##INTRo to YAML
-`YAML`: YAML Ain't Markup language
-`YAML`: represents data through key-value pairs

##Key-Value Pairs

---     -> indicates the start of the documents

192.168.1.0/24: Ethernet1/1 -> in YAML colon is used to distinguish between Key & value.

Key comes before the colon & value comes after the colon

---
192.168.1.0/24:
  - Ethernet1/1 -> Used two (space) after that (-)hypen character then agaon (space) then value Ethernet1/1
192.168.2.0/24:
  - Ethernet1/2

##Nesting in YAML
the power of key value pair is called nesting
Value of the key is another dictionary or a list of dictionaries

-`Below example of nesting in YAML`: 

---
192.168.1.0/24:
  - interface: Ethernet1/1
    next_hop: 10.10.0.1
192.168.2.0/24:
  - interface: Ethernet1/2
    next_hop: 10.10.0.3

## String Manipulation in YAML

motd: >
    You must have ex[;icit, autorized permission\n          -> we have used four (space) in beginining then \n at last
    access or configuration this device. Unautorized\n
    may result in civil or criminal penalities.

##Remember Unfolded & Folded YAML characters
-`Pipe (|)`:  Unfolded right angle bracket characters
 -`Right Anglr bracket (>)`:  Bent or folded Pipe character
