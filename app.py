import streamlit as st
import google.generativeai as genai
import json

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="EquiCare AI | Governance Layer", layout="wide")
st.title("🩺 EquiCare AI: Comprehensive AI Governance Layer")
st.markdown("Providing **Pre-Model Data Auditing** and **Post-Model Explainability Traces**.")

# --- API SETUP ---
# The API key is now hardcoded; sidebar input has been removed.
# --- API SETUP ---
# Securely fetch the API key from Streamlit secrets
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-flash-lite-latest')
except KeyError:
    st.error("API Key not found. Please configure your secrets.")
    st.stop()

# --- TABS FOR PRE & POST MODEL AUDITING ---
tab1, tab2 = st.tabs(["📊 Phase 1: Pre-Model Data Audit", "🔍 Phase 2: Post-Model Explainability Trace"])

# ==========================================
# TAB 1: PRE-MODEL AUDIT (New Feature!)
# ==========================================
with tab1:
    st.header("Audit Historical Training Data")
    st.markdown("Ensure the foundational data is free of demographic skew *before* it trains a diagnostic model.")
    
    # Simulating a dataset upload/selection
    dataset_context = st.text_area(
        "Describe the Training Dataset (e.g., Cardiology Records 2015-2023):",
        "Dataset contains 10,000 cardiology patient records. 75% male, 25% female. Primary indicators weighted: severe chest pain, elevated troponin, left arm numbness."
    )
    
    if st.button("Run Pre-Model Data Audit", type="secondary"):
        with st.spinner("Gemini is auditing dataset parameters for historical bias..."):
            prompt = f"""
            You are an AI Governance Expert. Analyze this proposed medical training dataset for inherent biases.
            Dataset: {dataset_context}
            
            Provide a structured report:
            1. Demographic Skew Analysis (Who is underrepresented?)
            2. Feature Bias Risk (Are the primary indicators skewed toward one demographic?)
            3. Mitigation Strategy (How to balance this data before training)
            """
            try:
                response = model.generate_content(prompt)
                st.success("Pre-Model Audit Complete.")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")

# ==========================================
# TAB 2: POST-MODEL AUDIT (Our Upgraded Core)
# ==========================================
with tab2:
    st.header("Post-Model Decision & Explainability Trace")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Patient Context")
        age = st.number_input("Age", min_value=1, max_value=120, value=45)
        gender = st.selectbox("Gender", ["Female", "Male", "Non-Binary", "Other"])
        history = st.text_area("Medical History", "No prior cardiac events, family history of early-onset heart disease.")
        
        # Comprehensive list of symptoms covering multiple medical bias scenarios
        all_symptoms = [
            "unexplained fatigue", "jaw pain", "nausea", "shortness of breath", "chest pain", 
            "severe chest compression", "radiating left arm pain", "dizziness", "upper back pressure", 
            "indigestion", "irregular lesion borders", "localized itching", "changing lesion texture", 
            "sudden severe swelling", "blinding headaches", "elevated blood pressure at triage", 
            "chronic fatigue", "swollen ankles", "decreased urine output", "severe lower abdominal pain", 
            "fever", "vomiting"
        ]
        symptoms = st.multiselect("Symptoms", all_symptoms, default=["unexplained fatigue", "jaw pain", "nausea"])

    with col2:
        st.subheader("Black-Box Model Output")
        st.error("**Risk Score:** Low (12%)\n\n**Recommendation:** Routine follow-up. Discharged.")
        st.markdown("⚠️ *Governance Alert: Decision flagged for missing fairness metrics.*")

    st.divider()
    if st.button("Generate Explainability Trace", type="primary", use_container_width=True):
        with st.spinner("Generating retrospective audit trace via Gemini..."):
            patient_data = {"age": age, "gender": gender, "symptoms": symptoms, "history": history}
            
            prompt = f"""
            You are an AI Governance Auditor. Generate a 'Post-Model Explainability Trace' for this flagged decision.
            Patient: {json.dumps(patient_data)}
            Black-Box Prediction: "Low Risk. Discharged."

            Format strictly as:
            1. Explainability Breakdown (Why did the black-box model likely ignore the symptoms?)
            2. Fairness Metric Failure (Identify the specific bias)
            3. Retrospective Correction (The clinically accurate recommendation)
            """
            try:
                response = model.generate_content(prompt)
                st.success("Explainability Trace Generated.")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
