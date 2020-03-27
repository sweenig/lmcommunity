$hostname = "##HOSTNAME##"
$service = "##WILDVALUE##"
$wait = 5 # seconds to wait

#Stop-Service -InputObject $(Get-Service -Computer $hostname -Name $service)  # testing only
#Start-Sleep 4  # testing only

$service_status = (Get-Service -Name $service -ComputerName $hostname).Status
Write-Host "$service is $service_status on $hostname"

if ((get-service -name $service -ComputerName $hostname).Status -eq "Running") {
  write-host "result_code: 1 (running)"
} else {
  Write-Host "not running so i will start then wait $wait seconds and test"
  Start-Service -InputObject $(Get-Service -Computer $hostname -Name $service)
  Start-Sleep $wait

  #Stop-Service -InputObject $(Get-Service -Computer $hostname -Name $service) # testing only
  #Start-Sleep 4 # testing only

  if ((get-service -name $service -ComputerName $hostname).Status  -eq "Running") {
        write-host "result_code: 2 (first restart worked)"
    } else {
        Write-Host "first restart failed so i will start second time"
        Start-Service -InputObject $(Get-Service -Computer $hostname -Name $service)
        Start-Sleep $wait

        #Stop-Service -InputObject $(Get-Service -Computer $hostname -Name $service) # testing only
        #Start-Sleep 3 # testing only

        if ((get-service -name $service -ComputerName $hostname).Status  -eq "Running") {
            Write-Host "result_code: 3 (second restart worked)"
        } else {
            Write-Host "result_code: 4 (second restart failed so probably trigger alert)"
        } # end of else line 21
    } # end of else line 15
} # end of line 9