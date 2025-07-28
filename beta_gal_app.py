import streamlit as st

class beta_gal_assay:
    def __init__(self, num_of_wells):
        self.num_of_wells = int(num_of_wells)

        # For subclasses
        self.area = None
        self.media_volume = None
        self.working_volume = None

    def get_PBS_preparation(self):
        first_rinse = self.media_volume * self.num_of_wells
        second_rinse = self.media_volume * self.num_of_wells
        third_rinse = self.media_volume * self.num_of_wells
        
        total_volume_of_1X_PBS = first_rinse + second_rinse + third_rinse
        dilute_guide_1X_PBS = {
            'Water': total_volume_of_1X_PBS * 0.9,
            '10X_PBS': total_volume_of_1X_PBS * 0.1 
        }
        return dilute_guide_1X_PBS

    def get_Fixative_Solution_preparation(self):
        required_1X_Fixative_Solution = self.working_volume * self.num_of_wells
        dilute_guide_1X_Fixative_Solution = {
            'Water': required_1X_Fixative_Solution * 0.9,
            '10X Fixative Solution': required_1X_Fixative_Solution * 0.1
        } 
        return dilute_guide_1X_Fixative_Solution

    def get_beta_galactosidase_Staining_Solution_preparation(self):
        required_1X_Staining_Solution = self.working_volume *0.93 * self.num_of_wells
        required_100X_Solution_A = self.working_volume *0.01 * self.num_of_wells
        required_100X_Solution_B = self.working_volume *0.01 * self.num_of_wells
        required_Xgal_stock_solution = self.working_volume *0.05 * self.num_of_wells

        dilute_guide_beta_gal_solution = {
            '10X Staining Solution' : required_1X_Staining_Solution *0.1,
            'Water':required_1X_Staining_Solution *0.9,
            '100X Solution A': required_100X_Solution_A,
            '100X Solution B': required_100X_Solution_B,
            'X-gal powder': required_Xgal_stock_solution * 20, #mg
            'DMSO': required_Xgal_stock_solution
        }
        return dilute_guide_beta_gal_solution

    def get_protocol(self):
        protocol = f'''1. Remove growth media in each well.
2. Rinse each well once with {self.media_volume*1000}μl of 1X PBS.
3. Add {self.working_volume*1000:.0f}μl of 1X Fixative Solution.
4. Stay it in room temperature for 10-15 minutes.
5. Rinse each well twice with {self.media_volume*1000}μl of 1X PBS.
6. Add {self.working_volume*1000}μl of β-galactosidase Staining Solution for each well.
7. Seal the plate with parafilm.
8. Incubate the plate in 37°C dry incubator overnight (12-16h).'''
        return protocol

# Classes for each culturing dish or plate
class six_well(beta_gal_assay):
    def __init__(self, num_of_wells):
        super().__init__(num_of_wells)
        self.area = 9.6  # cm²
        self.media_volume = 2.0  # ml
        self.working_volume = self.media_volume / 2  # ml

class twelve_well(beta_gal_assay):
    def __init__(self, num_of_wells):
        super().__init__(num_of_wells)
        self.area = 3.5  # cm²
        self.media_volume = 1.0  # ml
        self.working_volume = self.media_volume / 2  # ml

class twenty_four_well(beta_gal_assay):
     def __init__(self, num_of_wells):
        super().__init__(num_of_wells)
        self.area = 1.9  # cm²
        self.media_volume = 0.5  # ml
        self.working_volume = self.media_volume / 2  # ml

class hundred_pi_dish(beta_gal_assay):
     def __init__(self, num_of_wells):
        super().__init__(num_of_wells)
        self.area = 56.7  # cm²
        self.media_volume = 8  # ml
        self.working_volume = self.media_volume / 2  # ml

# Streamlit App
def main():
    st.set_page_config(
        page_title="β-Gal Assay Calc",
        page_icon="🧪",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS for mobile optimization
    st.markdown("""
    <style>
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 100%;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 0.5rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
    }
    h1 {
        font-size: 1.5rem !important;
        margin-bottom: 1rem !important;
    }
    h2 {
        font-size: 1.2rem !important;
        margin-bottom: 0.5rem !important;
        margin-top: 1rem !important;
    }
    h3 {
        font-size: 1rem !important;
        margin-bottom: 0.5rem !important;
    }
    .stSelectbox label {
        font-size: 0.9rem !important;
    }
    .stNumberInput label {
        font-size: 0.9rem !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("🧪 β-Gal Assay Calculator")
    
    # Input section at the top
    st.markdown("### Configuration")
    
    # Culture plate selection
    culture_options = {
        "6-well plate": ("6-well", six_well),
        "12-well plate": ("12-well", twelve_well),
        "24-well plate": ("24-well", twenty_four_well),
        "100π dish": ("100π dish", hundred_pi_dish)
    }
    
    selected_culture = st.selectbox(
        "Select plate/dish type:",
        list(culture_options.keys()),
        index=0
    )
    
    # Number of wells/dishes
    num_units = st.number_input(
        "Number of wells/dishes:",
        min_value=1,
        max_value=100,
        value=3,
        step=1
    )
    
    # Create the appropriate assay object
    culture_name, culture_class = culture_options[selected_culture]
    assay = culture_class(num_units)
    
    # Display plate information in a compact format
    st.info(f"**{culture_name}** • {num_units} units • {assay.area} cm²/well • {assay.media_volume} ml media")
    
    # Calculate solutions
    PBS = assay.get_PBS_preparation()
    fixative_sol = assay.get_Fixative_Solution_preparation()
    beta_gal_sol = assay.get_beta_galactosidase_Staining_Solution_preparation()
    
    # Solutions section - stacked vertically for mobile
    st.markdown("### 🧪 Solutions Required")
    
    # PBS Solution
    with st.expander("**1X PBS Solution**", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.metric("10X PBS", f"{PBS['10X_PBS']:.3f} ml")
        with col2:
            st.metric("Water", f"{PBS['Water']:.3f} ml")
    
    # Fixative Solution
    with st.expander("**1X Fixative Solution**", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.metric("10X Fixative", f"{fixative_sol['10X Fixative Solution']:.3f} ml")
        with col2:
            st.metric("Water", f"{fixative_sol['Water']:.3f} ml")
    
    # β-Galactosidase Staining Solution
    with st.expander("**β-Gal Staining Solution**", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.metric("10X Staining", f"{beta_gal_sol['10X Staining Solution']*1000:.0f} μl")
            st.metric("Solution A", f"{beta_gal_sol['100X Solution A']*1000:.0f} μl")
            st.metric("Solution B", f"{beta_gal_sol['100X Solution B']*1000:.0f} μl")
        with col2:
            st.metric("Water", f"{beta_gal_sol['Water']:.3f} ml")
            st.metric("X-gal powder", f"{beta_gal_sol['X-gal powder']:.3f} mg")
            st.metric("DMSO", f"{beta_gal_sol['DMSO']*1000:.0f} μl")
    
    # Protocol section
    st.markdown("### 📋 Protocol")
    protocol_text = assay.get_protocol()
    
    with st.expander("**Step-by-step protocol**", expanded=False):
        st.text(protocol_text)
    
    # Quick reference - compact summary
    st.markdown("### 📊 Quick Reference")
    
    # Create a more compact summary for mobile
    st.markdown(f"""
    **PBS Total:** {PBS['10X_PBS'] + PBS['Water']:.3f} ml (for 3 rinses)
    
    **Fixative Total:** {fixative_sol['10X Fixative Solution'] + fixative_sol['Water']:.3f} ml
    
    **Staining Total:** {(beta_gal_sol['10X Staining Solution'] + beta_gal_sol['Water'] + beta_gal_sol['100X Solution A'] + beta_gal_sol['100X Solution B'] + beta_gal_sol['DMSO'])*1000:.0f} μl
    """)
    
    # Important notes in a collapsible section
    with st.expander("⚠️ **Important Notes**"):
        st.markdown("""
        • Prepare X-gal stock by dissolving powder in DMSO
        • Keep staining solution protected from light
        • Use room temperature solutions
        • Incubation time may vary with expression level
        """)

if __name__ == "__main__":
    main()