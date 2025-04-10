import streamlit as st
import time

# Set page title
st.set_page_config(page_title="Countdown Timer", page_icon="⏱️")
st.title("Simple Countdown Timer")

# Initialize session state variables
if 'duration' not in st.session_state:
    st.session_state.duration = 60  # Default 60 seconds
if 'running' not in st.session_state:
    st.session_state.running = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'remaining' not in st.session_state:
    st.session_state.remaining = None
if 'paused' not in st.session_state:
    st.session_state.paused = False
if 'pause_start' not in st.session_state:
    st.session_state.pause_start = None
if 'total_pause_time' not in st.session_state:
    st.session_state.total_pause_time = 0

# Set timer duration
minutes = st.number_input("Minutes", min_value=0, max_value=60, value=1)
seconds = st.number_input("Seconds", min_value=0, max_value=59, value=0)
total_seconds = minutes * 60 + seconds

# Timer display
if st.session_state.running:
    # Calculate remaining time
    if st.session_state.paused:
        elapsed = st.session_state.remaining
    else:
        elapsed = time.time() - st.session_state.start_time - st.session_state.total_pause_time
        st.session_state.remaining = max(0, st.session_state.duration - elapsed)
    
    # Format time as MM:SS
    mins, secs = divmod(int(st.session_state.remaining), 60)
    time_format = f"{mins:02d}:{secs:02d}"
    
    # Display timer
    st.header(f"Time Remaining: {time_format}")
    
    # Progress bar
    progress = 1 - (st.session_state.remaining / st.session_state.duration)
    st.progress(min(1.0, progress))
    
    # Check if timer is complete
    if st.session_state.remaining <= 0 and not st.session_state.paused:
        st.success("Time's up!")
        st.balloons()
        st.session_state.running = False
    elif not st.session_state.paused:
        # Auto-refresh every second
        time.sleep(0.1)
        st.rerun()
else:
    st.header(f"Set Timer: {minutes:02d}:{seconds:02d}")

# Control buttons
col1, col2, col3 = st.columns(3)

with col1:
    if not st.session_state.running:
        if st.button("Start", use_container_width=True):
            st.session_state.duration = total_seconds
            st.session_state.running = True
            st.session_state.start_time = time.time()
            st.session_state.paused = False
            st.session_state.total_pause_time = 0
            st.rerun()

with col2:
    if st.session_state.running:
        if st.session_state.paused:
            if st.button("Resume", use_container_width=True):
                pause_duration = time.time() - st.session_state.pause_start
                st.session_state.total_pause_time += pause_duration
                st.session_state.paused = False
                st.rerun()
        else:
            if st.button("Pause", use_container_width=True):
                st.session_state.paused = True
                st.session_state.pause_start = time.time()
                st.rerun()

with col3:
    if st.session_state.running:
        if st.button("Reset", use_container_width=True):
            st.session_state.running = False
            st.session_state.paused = False
            st.session_state.start_time = None
            st.session_state.remaining = None
            st.session_state.total_pause_time = 0
            st.rerun()
