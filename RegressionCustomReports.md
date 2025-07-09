# Custom Reports – Key Regression Checks

1. **Static Date Range**  
   - **What to do:** Switch the date picker to a static range (e.g. “05 Dec ’24 – 31 Dec ’24”).  
   - **Why it matters:** Verifies that charts & tables reload exactly for the chosen fixed dates.  


2. **Compare-to-Day-Ago Overlay**  
   - **What to do:** Enable “Compare → Compare to Day ago.”  
   - **Why it matters:** Ensures the previous-period overlay appears correctly on the line chart.  



3. **AND / OR Filter Logic**  
   - **What to do:** Add two filters (e.g. `Clicks ≥ 0` AND `Cost per Install > 0`), then switch to OR.  
   - **Why it matters:** Confirms both logical connectors produce the correct subset of data.  


4. **Empty-State Handling**  
   - **What to do:** Apply a filter that yields no data (e.g. `Spend < 0`).  
   - **Why it matters:** Validates that the “Please select rows to display data” message shows and no table rows appear.  
  
<img width="862" alt="Screenshot 2025-07-09 at 16 31 32" src="https://github.com/user-attachments/assets/7d16c70e-95b7-48c7-9cf1-90f3d73ba9d7" />
<img width="872" alt="Screenshot 2025-07-09 at 16 30 46" src="https://github.com/user-attachments/assets/78f929e1-cd1e-471b-b23a-e6c5d3f5a5f0" />
<img width="887" alt="Screenshot 2025-07-09 at 16 30 00" src="https://github.com/user-attachments/assets/91d3692d-1437-4080-a94f-8dedb11f38b6" />
