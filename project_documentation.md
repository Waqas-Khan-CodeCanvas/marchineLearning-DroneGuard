# Drone Network Attack Detection System

## Simple Documentation

### What Does This Project Do?

This project helps protect drones from cyber attacks by watching the network traffic (like internet data) going to and from drones. It's like a security guard that watches for suspicious activity and alerts you when something doesn't look right.

### Main Parts of the Project

#### 1. The Brain (Machine Learning Model)

- **What it does**: Learns to tell the difference between normal drone traffic and attack traffic
- **How it works**:
  - Looks at things like packet size (how big the data is)
  - Checks what type of data is being sent (TCP or UDP)
  - Watches where the data is coming from and going to
  - Uses this information to spot unusual patterns

#### 2. The Control Center (Web Dashboard)

- **What it does**: Shows you what's happening in real-time
- **What you can see**:
  - Current status (Normal or Under Attack)
  - History of attacks in a simple graph
  - Alerts when attacks are detected

#### 3. The Connection (Backend System)

- **What it does**: Connects the Brain to the Control Center
- **How it works**:
  - Gets new data from the drone network
  - Sends it to the Brain for checking
  - Shows results on the Control Center

### How to Use the System

1. **Starting the System**

   ```bash
   # Install required tools
   pip install -r requirements.txt

   # Start the dashboard
   python app.py
   ```

2. **Viewing the Dashboard**

   - Open your web browser
   - Go to: http://localhost:8050
   - You'll see the main dashboard

3. **Testing the System**
   ```bash
   # Run the test script
   python test_detection.py
   ```

### What the System Detects

1. **Normal Traffic**

   - Regular communication patterns
   - Standard packet sizes
   - Expected protocols

2. **Suspicious Traffic**
   - Unusually large data packets
   - Unexpected communication patterns
   - Strange source addresses

### Files in the Project

1. **`ml_model.py`**

   - Contains the Brain of the system
   - Handles attack detection

2. **`app.py`**

   - Runs the dashboard
   - Shows the results

3. **`test_detection.py`**

   - Helps test if everything is working
   - Sends sample traffic data

4. **`requirements.txt`**
   - Lists all the tools needed

### How It Helps

1. **Real-Time Protection**

   - Watches drone traffic constantly
   - Alerts immediately when attacks are detected

2. **Easy to Understand**

   - Simple dashboard layout
   - Clear alerts
   - Visual history of events

3. **Simple to Use**
   - Just start the system and open the dashboard
   - Everything updates automatically
   - No complex settings needed

### Technical Details (Simplified)

1. **Machine Learning Model**

   - Uses Random Forest (like a group of decision-making trees)
   - Trained on real drone network data
   - Learns patterns to spot attacks

2. **Dashboard Features**

   - Real-time status updates
   - Attack history graph
   - Simple alert system

3. **Data Processing**
   - Automatically handles different types of network data
   - Cleans and prepares data for analysis
   - Updates in real-time

### Testing the System

1. **Sample Test Data**

   ```python
   # Example of normal traffic
   {
       "packet_size": 1024,
       "protocol": "TCP",
       "source_ip": "192.168.1.100"
   }
   ```

2. **What to Watch For**
   - Dashboard updates
   - Alert messages
   - Graph changes

### Future Improvements

1. **Possible Additions**

   - Email alerts
   - More detailed attack information
   - Custom alert settings

2. **Customization Options**
   - Add new types of attack detection
   - Modify dashboard layout
   - Change alert settings

### Need Help?

The system is designed to be simple, but if you need help:

1. Check if all files are present
2. Make sure all requirements are installed
3. Verify the dashboard is running
4. Look for any error messages in the console

Remember: This system is meant to be simple and easy to understand while still providing effective drone network protection.
