import streamlit as st
import time
import matplotlib.pyplot as plt
import graphviz

# ----------------------------
st.set_page_config(page_title="Streamlit App Development Guide", layout="wide")

st.title("🚀 Streamlit App Development and Deployment Guide")

# Sidebar for Navigation
page = st.sidebar.selectbox("Choose a Topic", [
    "📋 Step-by-Step Process",
    "📈 Flowchart of App Lifecycle",
    "🧠 Required Tools and Platforms",
    "🧪 Sample Streamlit App Code",
    "🌐 How to Deploy on the Internet",
    "📊 Progress Tracker"
])

# ----------------------------
if page == "📋 Step-by-Step Process":
    st.header("📋 Step-by-Step Guide to Create a Streamlit App")

    steps = [
        "1️⃣ Install Python & Streamlit",
        "2️⃣ Write your App using Streamlit",
        "3️⃣ Run your App Locally",
        "4️⃣ Push the App to GitHub",
        "5️⃣ Deploy it on Streamlit Cloud or other platforms",
        "6️⃣ Share your app URL with others"
    ]
    for step in steps:
        st.success(step)
        time.sleep(0.5)

    st.info("Tip: Use `pip install streamlit` to get started!")

# ----------------------------
elif page == "📈 Flowchart of App Lifecycle":
    st.header("📈 App Lifecycle Flowchart")

    code = """
    digraph G {
        Python_Installed -> Streamlit_Installed
        Streamlit_Installed -> Code_App
        Code_App -> Run_Locally
        Run_Locally -> Push_GitHub
        Push_GitHub -> Deploy_StreamlitCloud
        Deploy_StreamlitCloud -> App_Live
    }
    """
    st.graphviz_chart(code)

# ----------------------------
elif page == "🧠 Required Tools and Platforms":
    st.header("🧠 Tools and Platforms You Need")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Software Required")
        st.markdown("- Python (>=3.7)")
        st.markdown("- Streamlit")
        st.markdown("- Git")
        st.markdown("- Code Editor (e.g., VSCode)")

    with col2:
        st.subheader("Platforms for Deployment")
        st.markdown("- [GitHub](https://github.com/)")
        st.markdown("- [Streamlit Cloud](https://streamlit.io/cloud)")
        st.markdown("- (Optional) Heroku, Render, AWS, GCP")

# ----------------------------
elif page == "🧪 Sample Streamlit App Code":
    st.header("🧪 Sample Streamlit App Code")

    st.code('''
# Save this as app.py
import streamlit as st

st.title("Hello Streamlit!")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Welcome, {name}! 👋")
    st.balloons()
''', language='python')

    st.markdown("To run this locally, open terminal and type:")
    st.code("streamlit run app.py")

# ----------------------------
elif page == "🌐 How to Deploy on the Internet":
    st.header("🌐 Deployment: How to Publish Your App Online")

    st.markdown("### Step 1: Push to GitHub")
    st.code("git init\ngit add .\ngit commit -m 'initial commit'\ngit remote add origin <repo-url>\ngit push -u origin main")

    st.markdown("### Step 2: Deploy on Streamlit Cloud")
    st.markdown("1. Go to [Streamlit Cloud](https://streamlit.io/cloud)")
    st.markdown("2. Sign in with GitHub")
    st.markdown("3. Click `New App` > Choose repo and `app.py`")
    st.markdown("4. Click `Deploy` 🚀")

    st.success("Your app will be live at: `https://your-app.streamlit.app`")

# ----------------------------
elif page == "📊 Progress Tracker":
    st.header("📊 Track Your Progress")

    tasks = {
        "Installed Python": False,
        "Installed Streamlit": False,
        "Wrote Streamlit App": False,
        "Tested Locally": False,
        "Pushed to GitHub": False,
        "Deployed App": False
    }

    progress = 0
    for task in tasks:
        if st.checkbox(task):
            progress += 1

    st.progress(progress / len(tasks))

    fig, ax = plt.subplots()
    ax.barh(list(tasks.keys()), [1 if st.session_state.get(t, False) else 0 for t in tasks])
    ax.set_xlim(0, 1)
    ax.set_title("Task Completion Status")
    st.pyplot(fig)

# ----------------------------
st.sidebar.markdown("---")
st.sidebar.markdown("Developed by **Rohit Maurya**")
st.sidebar.markdown("Dept. of Civil Engineering, HCST Mathura")
