#!/bin/bash
current_time=$(date +"%H:%M")
end_time="18:00"
remaining_time=$(echo "$(( ($(date -d "$end_time" +%s) - $(date +%s)) / 3600 ))hours $(( ($(date -d "$end_time" +%s) - $(date +%s)) % 3600 / 60 ))minutes")

echo "Current time: $current_time"
echo "Work day ends after: $remaining_time"
