import os
import subprocess
import sys
import time
import win32com.client
import win32net
import wx

filename = r"C:\Users\pbabar4\Music\iplist.txt"

class RedirectText:
    def __init__(self,aWxTextCtrl):
        self.out=aWxTextCtrl
        
        if not os.path.exists(r"C:\logs"):
            os.mkdir(r"C:\logs")
        self.filename = open(filename, "w")

    def write(self,string):
        self.out.WriteText(string)
        if self.filename.closed:
            pass
        else:
            self.filename.write(string)
 
class MyForm(wx.Frame):

    #---------------------------------------------------------------------- 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Diagnostic Tool")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        log = wx.TextCtrl(panel, wx.ID_ANY, size=(300,100),
                          style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        # log.Disable()
        btn = wx.Button(panel, wx.ID_ANY, 'Run Diagnostics')
        self.Bind(wx.EVT_BUTTON, self.onRun, btn)

        # Add widgets to a sizer        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(log, 1, wx.ALL|wx.EXPAND, 5)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)

        # redirect text here
        self.redir=RedirectText(log)
        sys.stdout=self.redir
    
    #----------------------------------------------------------------------    
    def runDiagnostics(self):
        """
        Run some diagnostics to get the machine name, ip address, mac,
        gateway, DNS, route tables, etc
        """
        # create the route table:
        # based on the following list comp from http://win32com.goermezer.de/content/view/220/284/
        # route_table = [elem.strip().split() for elem in os.popen("route print").read().split("Metric\n")[1].split("\n") if re.match("^[0-9]", elem.strip())]
        route_table = []
        proc = subprocess.Popen("route print", shell=True,
                        stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()
            route_table.append(line.strip().split())
            if not line: break
        proc.wait()
        
        print "Log Created at %s" % time.ctime()
        print "----------------------------------------------------------------------------------------------"
        info = win32net.NetWkstaGetInfo(None, 102)
        self.compname = info["computername"]
        print "Computer name: %s\n" % self.compname
        
        print "----------------------------------------------------------------------------------------------"
        print "Route Table:"
        print "%20s\t %15s\t %15s\t %15s\t %s" % ("Network Destination", "Netmask",
                                          "Gateway", "Interface", "Metric")
        for route in route_table:
            if len(route) == 5:
                dst, mask, gateway, interface, metric = route
                print "%20s\t %15s\t %15s\t %15s\t %s" % (dst, mask, gateway, interface, metric)
            
        print "----------------------------------------------------------------------------------------------\n"
        ips = ["65.55.17.26", "67.205.46.185", "67.195.160.76"]
        for ip in ips:
            self.pingIP(ip)
            print
            self.tracertIP(ip)
            print "\n----------------------------------------------------------"
        self.getNICInfo()
        print "############ END OF LOG ############"
     
    #----------------------------------------------------------------------   
    def pingIP(self, ip):
        proc = subprocess.Popen("ping %s" % ip, shell=True, 
                                stdout=subprocess.PIPE) 
        print
        while True:
            line = proc.stdout.readline()                        
            wx.Yield()
            if line.strip() == "":
                pass
            else:
                print line.strip()
            if not line: break
        proc.wait()
    
    #----------------------------------------------------------------------
    def tracertIP(self, ip):
        proc = subprocess.Popen("tracert -d %s" % ip, shell=True, 
                                stdout=subprocess.PIPE)
        print 
        while True:
            line = proc.stdout.readline()
            wx.Yield()
            if line.strip() == "":
                pass
            else:
                print line.strip()
            if not line: break
        proc.wait()

    #----------------------------------------------------------------------            
    def getNICInfo(self):
        """
        http://www.microsoft.com/technet/scriptcenter/scripts/python/pyindex.mspx?mfr=true
        """
        print "\nInterface information:\n"
        strComputer = "."
        objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_NetworkAdapterConfiguration")
        numOfNics = len(colItems)
        count = 1
        for objItem in colItems:
            # if the IP interface is enabled, grab its info
            print "***Interface %s of %s***" % (count, numOfNics)
            if objItem.IPEnabled == True:                
                print "Arp Always Source Route: ", objItem.ArpAlwaysSourceRoute
                print "Arp Use EtherSNAP: ", objItem.ArpUseEtherSNAP
                print "Caption: ", objItem.Caption
                print "Database Path: ", objItem.DatabasePath
                print "Dead GW Detect Enabled: ", objItem.DeadGWDetectEnabled
                z = objItem.DefaultIPGateway
                if z is None:
                    a = 1
                else:
                    for x in z:
                        print "Default IP Gateway: ", x
                print "Default TOS: ", objItem.DefaultTOS
                print "Default TTL: ", objItem.DefaultTTL
                print "Description: ", objItem.Description
                print "DHCP Enabled: ", objItem.DHCPEnabled
                print "DHCP Lease Expires: ", objItem.DHCPLeaseExpires
                print "DHCP Lease Obtained: ", objItem.DHCPLeaseObtained
                print "DHCP Server: ", objItem.DHCPServer
                print "DNS Domain: ", objItem.DNSDomain
                z = objItem.DNSDomainSuffixSearchOrder
                if z is None:
                    a = 1
                else:
                    for x in z:
                        print "DNS Domain Suffix Search Order: ", x
                print "DNS Enabled For WINS Resolution: ", objItem.DNSEnabledForWINSResolution
                print "DNS Host Name: ", objItem.DNSHostName
                z = objItem.DNSServerSearchOrder
                if z is None:
                    a = 1
                else:
                    for x in z:
                        print "DNS Server Search Order: ", x
                print "Domain DNS Registration Enabled: ", objItem.DomainDNSRegistrationEnabled
                print "Forward Buffer Memory: ", objItem.ForwardBufferMemory
                print "Full DNS Registration Enabled: ", objItem.FullDNSRegistrationEnabled
                z = objItem.GatewayCostMetric
                if z is None:
                    a = 1
                else:
                    for x in z:
                        print "Gateway Cost Metric: ", x
                print "IGMP Level: ", objItem.IGMPLevel
                print "Index: ", objItem.Index
                z = objItem.IPAddress
                if z is None:
                    a = 1
                else:
                    for x in z:
                        print "IP Address: ", x
                print "IP Connection Metric: ", objItem.IPConnectionMetric
                print "IP Enabled: ", objItem.IPEnabled
                print "IP Filter Security Enabled: ", objItem.IPFilterSecurityEnabled
                print "IP Port Security Enabled: ", objItem.IPPortSecurityEnabled
                z = objItem.IPSecPermitIPProtocols
                if z is None:
                    a = 1
                else:
                    for x in z:
                        print "IP Sec Permit IP Protocols: ", x
                z = objItem.IPSecPermitTCPPorts
                if z is None:
                    a = 1
                else:
                    for x in z:
                        print "IP Sec Permit TCP Ports: ", x
                z = objItem.IPSecPermitUDPPorts
                if z is None:
                    a = 1
                else:
                    for x in z:
                        print "IPSec Permit UDP Ports: ", x
                z = objItem.IPSubnet
                if z is None:
                    a = 1
                else:
                    for x in z:
                        print "IP Subnet: ", x
                print "IP Use Zero Broadcast: ", objItem.IPUseZeroBroadcast
                print "IPX Address: ", objItem.IPXAddress
                print "IPX Enabled: ", objItem.IPXEnabled
                z = objItem.IPXFrameType
                if z is None:
                    a = 1
                else:
                    for x in z:
                        print "IPX Frame Type: ", x
                print "IPX Media Type: ", objItem.IPXMediaType
                z = objItem.IPXNetworkNumber
                if z is None:
                    a = 1
                else:
                    for x in z:
                        print "IPX Network Number: ", x
                print "IPX Virtual Net Number: ", objItem.IPXVirtualNetNumber
                print "Keep Alive Interval: ", objItem.KeepAliveInterval
                print "Keep Alive Time: ", objItem.KeepAliveTime
                print "MAC Address: ", objItem.MACAddress
                print "MTU: ", objItem.MTU
                print "Num Forward Packets: ", objItem.NumForwardPackets
                print "PMTUBH Detect Enabled: ", objItem.PMTUBHDetectEnabled
                print "PMTU Discovery Enabled: ", objItem.PMTUDiscoveryEnabled
                print "Service Name: ", objItem.ServiceName
                print "Setting ID: ", objItem.SettingID
                print "Tcpip Netbios Options: ", objItem.TcpipNetbiosOptions
                print "Tcp Max Connect Retransmissions: ", objItem.TcpMaxConnectRetransmissions
                print "Tcp Max Data Retransmissions: ", objItem.TcpMaxDataRetransmissions
                print "Tcp Num Connections: ", objItem.TcpNumConnections
                print "Tcp Use RFC1122 Urgent Pointer: ", objItem.TcpUseRFC1122UrgentPointer
                print "Tcp Window Size: ", objItem.TcpWindowSize
                print "WINS Enable LMHosts Lookup: ", objItem.WINSEnableLMHostsLookup
                print "WINS Host Lookup File: ", objItem.WINSHostLookupFile
                print "WINS Primary Server: ", objItem.WINSPrimaryServer
                print "WINS Scope ID: ", objItem.WINSScopeID
                print "WINS Secondary Server: ", objItem.WINSSecondaryServer
                print "-------------------------------------------------------\n"
            else:
                print "Interface is disabled!\n"
            count += 1

    #----------------------------------------------------------------------
    def onRun(self, event):
        self.runDiagnostics()
        self.redir.filename.close()
        # Restore stdout to normal
        sys.stdout = sys.__stdout__

#----------------------------------------------------------------------         
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()