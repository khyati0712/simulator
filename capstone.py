import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Circuit Lab | Virtual Engineering Laboratory",
    page_icon="⚡",
    layout="wide"
)

# Custom styling
st.markdown("""
<style
.stApp {
    background-color: #FFFFFF;
    color: #000000;
}

h1, h2, h3, h4, h5, h6 {
    color: #000000;
}

p, li, label, span {
    color: #000000;
}

[data-testid="stSidebar"] {
    background-color: #F5F5F5;
}

[data-testid="stSidebar"] * {
    color: #000000;
}

.stMarkdown {
    color: #000000;
}

</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("⚡ CIRCUIT LAB")
st.sidebar.caption("Virtual Engineering Laboratory")

page = st.sidebar.radio(
    "MENU",
    ["Home", "Theory", "Procedure", "Virtual Lab", "Graph Analysis"]
)

# HOME PAGE
if page == "Home":

    st.markdown("""
    <div class="hero">
        <h1>Explore Electrical Engineering.</h1>
        <p>
        Understand circuits through theory, interactive experiments
        and real-time mathematical analysis.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("The Experiment")

    st.markdown("""
    Welcome to the virtual laboratory for **Thevenin's Theorem
    and Maximum Power Transfer**.

    Explore how a complex electrical network can be simplified
    into an equivalent circuit, and discover how maximum power
    is transferred to a load.
    """)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>📘 Theory</h3>
            <p>Understand the principles and mathematical foundations.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>⚡ Virtual Lab</h3>
            <p>Experiment with circuit parameters interactively.</p>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div class="info-card">
            <h3>📊 Observations</h3>
            <p>Record experimental readings and download your results.</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="info-card">
            <h3>📈 Analysis</h3>
            <p>Visualise the relationship between load resistance and power.</p>
        </div>
        """, unsafe_allow_html=True)

# PLACEHOLDER PAGES
elif page == "Theory":
    st.title("Theory")
    st.markdown("""
Electrical circuits often contain multiple voltage sources, resistors, and other components, making their analysis complicated. Network theorems simplify these complex circuits and make it easier to determine electrical quantities such as voltage, current, and power.
Thevenin's Theorem is one such technique that simplifies a linear electrical network into an equivalent circuit consisting of a single voltage source in series with a resistance. Maximum Power Transfer Theorem uses this equivalent circuit to determine the load resistance at which the power delivered to the load is maximum.
These two theorems are widely used in electrical circuit analysis, electronic system design, and power-related applications.
    
## What is Thevenin's Theorem?
Thevenin's Theorem states that any linear, bilateral two-terminal network containing voltage sources, current sources, and resistances can be replaced by an equivalent circuit consisting of a single ideal voltage source, known as Thevenin voltage ( $V_{Th}$), connected in series with an equivalent resistance, known as Thevenin resistance ( $R_{Th}$).
This equivalent circuit produces the same voltage and current at the load terminals as the original network.
#### Important terms:
- Thevenin Voltage ( $V_{Th}$): The open-circuit voltage measured across the load terminals when the load is disconnected.
- Thevenin Resistance ( $R_{Th}$): The equivalent resistance measured looking into the load terminals after deactivating all independent sources.
- Load Resistance ( $R_{L}$): The resistance connected across the output terminals of the equivalent circuit. 


## What is Maximum Power Transfer Theorem?
Maximum Power Transfer Theorem states that maximum power is delivered from a linear source network to a load when the load resistance is equal to the Thevenin resistance of the source network.

$R_{L}$=$R_{Th}$

This condition is known as the maximum power transfer condition for a DC resistive circuit.


## Practical significance and applications
-Communication systems: Impedance matching between transmitters, transmission lines, and antennas.

-Audio systems: Matching amplifier output impedance with connected equipment.

-Electronic circuits: Optimising power delivery between circuit stages.

-Signal transmission: Reducing signal reflections through impedance matching.

    """)

elif page == "Procedure":
    st.title("Procedure")
    st.markdown("""
## Procedure for Thevenin's Equivalent Circuit
1. Identify the load resistance and disconnect it from the circuit.

2. Calculate the open-circuit voltage across the load terminals.

3. Deactivate all independent sources:
    - Replace ideal independent voltage sources with short circuits.
    - Replace ideal independent current sources with open circuits.

4. Calculate the equivalent resistance looking into the open load terminals.

5. Replace the original network with an ideal voltage source.

6. Reconnect the load resistance to the equivalent circuit.

## Procedure to prove the Maximum Power Transfer Theorem
1. Determine the Thevenin voltage ($V_{Th}$) and Thevenin resistance ($R_{Th}$) of the equivalent circuit.
2. Set the load resistance equal to the Thevenin resistance:
$R_L$ = $R_{Th}$

3. Connect the load resistance to the equivalent circuit.

4. Calculate the load current:
 $I_L = \\frac{V_{Th}}{R_{Th}+R_L}$

5. Calculate the load voltage:
$V_L$=$I_L$($R_L$)

6. Calculate the maximum power delivered to the load:
 $P_{max} = \\frac{V_{Th}^2}{4R_{Th}}$


7. Verify the result by varying ($R_L$) and observing that maximum power occurs when $R_L$=$R_{Th}$.

""")

elif page == "Virtual Lab":

    st.title("Virtual Laboratory")

    st.write(
        "Explore the Thevenin equivalent circuit "
        "and investigate Maximum Power Transfer."
    )

    st.subheader("1. Interactive Circuit Simulator")

    components.html(
        """
        <iframe
            src="https://www.falstad.com/s.py?s=pR97C8"
            width="100%"
            height="650"
            style="border: none;"
        ></iframe>
        """,
        height=670,
        scrolling=True
    )
    st.divider()

    # INITIALISE OBSERVATION TABLE
    if "observations" not in st.session_state:
        st.session_state.observations = pd.DataFrame(
            columns=[
                "Trial",
                "Load Resistance (Ω)",
                "Current (mA)",
                "Voltage (V)",
                "Power (mW)"
            ]
        )

    # OBSERVATION FORM
    st.subheader("2. Record Experimental Readings")

    st.write(
        "Adjust the load resistance in the simulator, "
        "observe the meter readings and enter them below."
    )

    with st.form("trial_form"):

        col1, col2 = st.columns(2)

        with col1:
            RL = st.number_input(
                "Load Resistance (Ω)",
                min_value=0.1,
                value=1000.0
            )

            current = st.number_input(
                "Load Current (mA)",
                min_value=0.0,
                value=5.4
            )

        with col2:
            voltage = st.number_input(
                "Load Voltage (V)",
                min_value=0.0,
                value=5.4
            )

        submitted = st.form_submit_button(
            "Add Trial",
            use_container_width=True
        )

    if submitted:

        power = current * voltage

        new_trial = pd.DataFrame([{
            "Trial": len(st.session_state.observations) + 1,
            "Load Resistance (Ω)": RL,
            "Current (mA)": current,
            "Voltage (V)": voltage,
            "Power (mW)": power
        }])

        st.session_state.observations = pd.concat(
            [st.session_state.observations, new_trial],
            ignore_index=True
        )

        st.success("Trial added successfully!")

    st.divider()

    # OBSERVATION TABLE
    st.subheader("3. Recorded Observations")

    if not st.session_state.observations.empty:

        st.dataframe(
            st.session_state.observations,
            use_container_width=True,
            hide_index=True
        )

        csv = st.session_state.observations.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "Download Observation Table (CSV)",
            data=csv,
            file_name="thevenin_observations.csv",
            mime="text/csv"
        )

        if st.button("Clear All Trials"):
            st.session_state.observations = pd.DataFrame(
                columns=[
                    "Trial",
                    "Load Resistance (Ω)",
                    "Current (mA)",
                    "Voltage (V)",
                    "Power (mW)"
                ]
            )
            st.rerun()

    else:
        st.info(
            "No observations recorded yet. "
            "Complete your first trial to get started!"
        )


elif page == "Graph Analysis":

    st.title("Graph for Maximum Power Transfer Theorem")

    st.write(
        "Analyse the relationship between load resistance and load power to verify the Maximum Power Transfer Theorem."
    )

    # Retrieve observations
    if (
        "observations" not in st.session_state
        or st.session_state.observations.empty
    ):

        st.info(
            "No experimental readings found. "
            "Please complete some trials in the Virtual Lab first."
        )

    else:

        df = st.session_state.observations.copy()

        # Identify maximum power
        max_index = df["Power (mW)"].idxmax()
        max_trial = df.loc[max_index]

        max_power = max_trial["Power (mW)"]
        max_resistance = max_trial["Load Resistance (Ω)"]

        st.subheader("1. Maximum Power Transfer Results")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Maximum Load Power",
            f"{max_power:.3f} mW"
        )

        col2.metric(
            "Load Resistance",
            f"{max_resistance:.2f} Ω"
        )

        col3.metric(
            "Trial Number",
            int(max_trial["Trial"])
        )

        st.divider()

        # Graph
        st.subheader("2. Load Power vs Load Resistance")

        fig = px.line(
            df.sort_values("Load Resistance (Ω)"),
            x="Load Resistance (Ω)",
            y="Power (mW)",
            markers=True,
            title="Variation of Load Power with Load Resistance"
        )

        # Highlight maximum power point
        fig.add_scatter(
            x=[max_resistance],
            y=[max_power],
            mode="markers",
            name="Maximum Power Point",
            marker=dict(
                color="black",
                size=12,
                symbol="circle"
            )
        )

        fig.update_layout(
            template="plotly_white",
            xaxis_title="Load Resistance (Ω)",
            yaxis_title="Load Power (mW)",
            plot_bgcolor="white",
            paper_bgcolor="white",
            font=dict(color="black")
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        # Observation table
        st.subheader("3. Experimental Data")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        # Conclusion
        st.subheader("4. Experimental Conclusion")

        st.write(
            f"The maximum recorded load power is "
            f"**{max_power:.3f} mW**, obtained at a load "
            f"resistance of **{max_resistance:.2f} Ω**."
        )
