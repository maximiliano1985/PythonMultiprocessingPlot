#!/usr/bin/env ruby

# trap ctrl+\ signal
Signal.trap (:QUIT) do
  puts "\nMain Process PID #{$$}\nChild Process PID #{pid}"
end
  
pid = fork do
  Kernel.system "./lib/visual.py"
end

Kernel.system "./lib/logg.py"

Process.wait2
