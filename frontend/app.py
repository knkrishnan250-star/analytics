import streamlit as st
import requests
import matplotlib.pyplot as plt
mechanism = st.sidebar.selectbox("Noise Mechanism", ["laplace", "gaussian"])
st.set_page_config(page_title="Privacy Analytics Engine", layout="wide")
params={"epsilon": epsilon, "mechanism": mechanism}
st.title("🔐 Privacy-Preserving Analytics Dashboard")

st.sidebar.title("Privacy Controls")
epsilon = st.sidebar.slider("Epsilon (Privacy Level)", 0.1, 5.0, 1.0)
st.sidebar.info("Lower epsilon = More Privacy\nHigher epsilon = More Accuracy")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    response = requests.post(
        "http://127.0.0.1:8000/upload/",
        files={"file": uploaded_file},
        params={"epsilon": epsilon}
    )

    if response.status_code == 200:
        result = response.json()

        st.sidebar.success(f"Remaining Budget: {result['remaining_budget']}")

        st.subheader("📊 Private Row Count")
        st.success(result["private_count"])

        for col, stats in result.items():
            if col in ["private_count", "remaining_budget"]:
                continue

            st.subheader(f"Column: {col}")
            st.write("Private Mean:", stats["mean"])
            st.write("Private Sum:", stats["sum"])

            noisy_counts, bin_edges = stats.get("histogram", (None, None))
            if noisy_counts:
                fig, ax = plt.subplots()
                ax.bar(range(len(noisy_counts)), noisy_counts)
                ax.set_title(f"Private Histogram - {col}")
                st.pyplot(fig)

    else:
        st.error(response.text)

st.sidebar.progress(result["remaining_budget"] / 5.0)

if st.sidebar.button("🔄 Reset Privacy Budget"):
    requests.post("http://127.0.0.1:8000/reset-budget/")
    st.sidebar.success("Budget Reset!")

st.subheader("📜 Query Audit Log")

logs = requests.get("http://127.0.0.1:8000/logs/").json()

for log in logs[::-1]:
    st.write(log)

if st.button("🤖 Run Federated Learning Simulation"):
    response = requests.post(
        "http://127.0.0.1:8000/federated/",
        files={"file": uploaded_file}
    )
    st.write(response.json())