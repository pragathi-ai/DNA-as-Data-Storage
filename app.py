import streamlit as st

# -----------------------------
# DNA DATA STORAGE DEMO
# -----------------------------

st.set_page_config(
    page_title="DNA Data Storage",
    page_icon="🧬",
    layout="wide"
)

# DNA mapping: 2 bits -> one DNA base
BITS_TO_DNA = {
    "00": "A",
    "01": "C",
    "10": "G",
    "11": "T"
}

DNA_TO_BITS = {v: k for k, v in BITS_TO_DNA.items()}


def text_to_binary(text):
    """Convert UTF-8 text into a binary string."""
    data = text.encode("utf-8")
    return "".join(format(byte, "08b") for byte in data)


def binary_to_dna(binary):
    """Convert binary into DNA bases using 2 bits per base."""
    # Add zeros if needed so the length is a multiple of 2
    if len(binary) % 2 != 0:
        binary += "0"

    return "".join(
        BITS_TO_DNA[binary[i:i + 2]]
        for i in range(0, len(binary), 2)
    )


def dna_to_binary(dna):
    """Convert DNA bases back into binary."""
    return "".join(DNA_TO_BITS[base] for base in dna)


def binary_to_text(binary):
    """Convert binary back into UTF-8 text."""
    # Keep only complete bytes
    usable_length = (len(binary) // 8) * 8
    binary = binary[:usable_length]

    data = bytes(
        int(binary[i:i + 8], 2)
        for i in range(0, len(binary), 8)
    )

    return data.decode("utf-8", errors="replace")


# -----------------------------
# Header
# -----------------------------

st.title("🧬 DNA as Data Storage")
st.subheader("Can We Store the Internet in DNA?")

st.markdown(
    """
This interactive demonstration shows the **basic principle of DNA data storage**:

**Text → Binary → DNA (A, C, G, T) → Binary → Original Text**
"""
)

st.divider()

# -----------------------------
# Input
# -----------------------------

st.markdown("### 1️⃣ Enter your digital message")

default_message = "KRCE PRESENTATION DAY"

message = st.text_input(
    "Type a message:",
    value=default_message,
    max_chars=100
)

if message:
    binary = text_to_binary(message)
    dna = binary_to_dna(binary)
    recovered_binary = dna_to_binary(dna)
    recovered_text = binary_to_text(recovered_binary)

    # -----------------------------
    # Step 1: Binary
    # -----------------------------

    st.markdown("### 2️⃣ Digital data → Binary")

    st.code(binary, language="text")

    st.caption(
        f"{len(message)} characters → {len(binary)} bits"
    )

    # -----------------------------
    # Step 2: DNA
    # -----------------------------

    st.markdown("### 3️⃣ Binary → DNA sequence")

    st.code(dna, language="text")

    st.caption(
        f"{len(dna)} DNA bases (A, C, G, T)"
    )

    # -----------------------------
    # Mapping
    # -----------------------------

    st.markdown("### 🧬 Our simple encoding rule")

    cols = st.columns(4)

    mapping_items = [
        ("00", "A"),
        ("01", "C"),
        ("10", "G"),
        ("11", "T")
    ]

    for col, (bits, base) in zip(cols, mapping_items):
        with col:
            st.metric(bits, base)

    # -----------------------------
    # Decode
    # -----------------------------

    st.markdown("### 4️⃣ DNA → Binary → Original message")

    st.code(recovered_binary, language="text")

    st.success(f"✅ Decoded message: **{recovered_text}**")

    # -----------------------------
    # Explanation
    # -----------------------------

    st.divider()
    st.markdown("### 💡 What did we demonstrate?")

    st.markdown(
        """
    - Computers represent information using **0 and 1**.
    - DNA uses four bases: **A, C, G and T**.
    - In this simplified demonstration, every **2 binary bits** are mapped to one DNA base.
    - The DNA sequence can then be decoded back into the original digital information.

    **Important:** This is an educational simulation of the encoding idea. Real DNA data
    storage requires DNA synthesis, sequencing, error correction, indexing, and specialized
    laboratory processes.
    """
    )

else:
    st.info("Enter a message above to start the demonstration.")

st.divider()

st.caption(
    "Presentation Demo • DNA Data Storage • From 0s & 1s to A, C, G & T"
)
