w_kip_per_ft = 10.0 # UDL
span_ft = 30.0      # simplly supported span

m_max_kip_ft = (w_kip_per_ft*span_ft**2)/8

print("Maximum bending:", m_max_kip_ft, "kip ft")