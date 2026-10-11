---
title: "47 CFR Part 11 — EMERGENCY ALERT SYSTEM (EAS)"
identifier: "47 CFR Part 11"
type: regulation
jurisdiction: us
language: en
last_amended: 2026-10-06  # latest amendment date of the CFR title
status: in_force
source: "https://www.ecfr.gov/current/title-47/part-11"
retrieved: 2026-10-11
ecfr_bulk_modified: "07-Oct-2026 21:20"
---

*Title 47—Telecommunication › CHAPTER I—FEDERAL COMMUNICATIONS COMMISSION › SUBCHAPTER A—GENERAL*

# PART 11—EMERGENCY ALERT SYSTEM (EAS)

**Authority:** 47 U.S.C. 151, 154 (i) and (n), 303(r), 544(g), 606, 1201, and 1206.

**Source:** 59 FR 67092, Dec. 28, 1994, unless otherwise noted.

## Subpart A—General

### § 11.1 Purpose.

This part contains rules and regulations providing for an Emergency Alert System (EAS). The EAS provides the President with the capability to provide immediate communications and information to the general public at the National, State and Local Area levels during periods of national emergency. The rules in this part describe the required technical standards and operational procedures of the EAS for analog AM, FM, and TV broadcast stations, digital broadcast stations, analog cable systems, digital cable systems, wireline video systems, wireless cable systems, Direct Broadcast Satellite (DBS) services, Satellite Digital Audio Radio Service (SDARS), and other participating entities. The EAS may be used to provide the heads of State and local government, or their designated representatives, with a means of emergency communication with the public in their State or Local Area.

[72 FR 62132, Nov. 2, 2007]

### § 11.2 Definitions.

The definitions of terms used in part 11 are:

(a) *National Emergency Message (EAN).* The National Emergency Message (formerly called the Emergency Action Notification or Presidential alert message) is the notice to all EAS Participants and to the general public that the EAS has been activated for a national emergency. EAN messages that are formatted in the EAS Protocol (specified in § 11.31) are sent from a government origination point to broadcast stations and other entities participating in the National Public Warning System, and are subsequently disseminated via EAS Participants. Dissemination arrangements for EAN messages that are formatted in the EAS Protocol (specified in § 11.31) at the State and local levels are specified in the State and Local Area plans (defined at § 11.21). A national activation of the EAS for a Presidential National Emergency Message with the Event code EAN as specified in § 11.31 must take priority over any other message and preempt it if it is in progress.

(b) *EAS Participants.* Entities required under the Commission's rules to comply with EAS rules, e.g., analog radio and television stations, and wired and wireless cable television systems, DBS, DTV, SDARS, digital cable and DAB, and wireline video systems.

(c) *Wireline Video System.* The system of a wireline common carrier used to provide video programming service.

(d) *Intermediary Device.* An intermediary device is a stand-alone device that carries out the functions of monitoring for, receiving and/or acquiring, and decoding EAS messages formatted in the Common Alerting Protocol (CAP) in accordance with § 11.56, and converting such messages into a format that can be inputted into a separate EAS decoder, EAS encoder, or unit combining such decoder and encoder functions, so that the EAS message outputted by such separate EAS decoder, EAS encoder, or unit combining such decoder and encoder functions, and all other functions attendant to processing such EAS message, comply with the requirements in this part.

[77 FR 16698, Mar. 22, 2012, as amended at 83 FR 37759, Aug. 2, 2018; 87 FR 67823, Nov. 10, 2022]

### § 11.11 The Emergency Alert System (EAS).

(a) The EAS is composed of analog radio broadcast stations including AM, FM, and Low-power FM (LPFM) stations; digital audio broadcasting (DAB) stations, including digital AM, FM, and Low-power FM stations; television (TV) broadcast stations, including Class A and low power TV (LPTV) stations; analog cable systems; digital cable systems which are defined for purposes of this part only as the portion of a cable system that delivers channels in digital format to subscribers at the input of a Unidirectional Digital Cable Product or other navigation device; wireline video systems; wireless cable systems which may consist of Broadband Radio Service (BRS), or Educational Broadband Service (EBS) stations; DBS services, as defined in § 25.701(a) of this chapter (including certain Ku-band Fixed-Satellite Service Direct to Home providers); and SDARS, as defined in § 25.201 of this chapter. These entities are referred to collectively as EAS Participants in this part, and are subject to this part, except as otherwise provided herein. At a minimum EAS Participants must use a common EAS protocol, as defined in § 11.31, to send and receive emergency alerts, and comply with the requirements set forth in § 11.56, in accordance with the following tables:

Table 1—Analog and Digital Broadcast Station Equipment Deployment Requirements

| EAS equipment requirement | AM & FM | Digital AM & FM | Analog & digital FM class D | Analog & digital LPFM | TV | Class A TV | LPTV |
|---|---|---|---|---|---|---|---|
| EAS decoder <sup>1</sup> | Y | Y | Y | Y | Y | Y | Y |
| EAS encoder | Y | Y | N | N | Y | Y | N |
| Audio message | Y | Y | Y | Y | Y | Y | Y |
| Video message | N/A | N/A | N/A | N/A | Y | Y | Y |

<sup>1</sup> EAS Participants may comply with the obligations set forth in § 11.56 to decode and convert CAP-formatted messages into EAS Protocol-compliant messages by deploying an Intermediary Device, as specified in § 11.56(b).

**Analog Cable Systems**

Analog cable systems are subject to the requirements in Table 2 below. Analog cable systems serving fewer than 5,000 subscribers from a headend may either provide the National level EAS message on all programmed channels including the required testing, or comply with the requirements in Table 2.

Table 2—Analog Cable System Equipment Deployment Requirements

| EAS equipment requirement | ≥5,000 subscribers | <5,000 subscribers |
|---|---|---|
| EAS decoder <sup>1</sup> | Y | Y |
| EAS encoder | Y | Y <sup>2</sup> |
| Audio and Video EAS Message on all channels | Y | N |
| Video interrupt and audio alert message on all channels; <sup>3</sup> Audio and Video EAS message on at least one channel | N | Y |

<sup>1</sup> EAS Participants may comply with the obligations set forth in § 11.56 to decode and convert CAP-formatted messages into EAS Protocol-compliant messages by deploying an Intermediary Device, as specified in § 11.56(b).

<sup>2</sup> Analog cable systems serving <5,000 subscribers are permitted to operate without an EAS encoder if they install an FCC-certified decoder.

<sup>3</sup> The Video interrupt must cause all channels that carry programming to flash for the duration of the EAS emergency message. The audio alert must give the channel where the EAS messages are carried and be repeated for the duration of the EAS message. [*Note:* Programmed channels do not include channels used for the transmission of data such as interactive games.]

**Wireless Cable Systems (BRS/EBS Stations)**

Wireless cable systems are subject to the requirements in Table 3 below. Wireless cable systems serving fewer than 5,000 subscribers from a single transmission site must either provide the National level EAS message on all programmed channels including the required testing, or comply with the requirements in Table 3.

Table 3—Wireless Cable System Equipment Deployment Requirements

| EAS equipment requirement | ≥5,000 subscribers | <5,000 subscribers |
|---|---|---|
| EAS decoder <sup>1</sup> | Y | Y |
| EAS encoder | Y | Y <sup>2</sup> |
| Audio and Video EAS Message on all channels <sup>3</sup> | Y | N |
| Video interrupt and audio alert message on all channels; <sup>4</sup> Audio and Video EAS message on at least one channel | N | Y |

<sup>1</sup> EAS Participants may comply with the obligations set forth in § 11.56 to decode and convert CAP-formatted messages into EAS Protocol-compliant messages by deploying an Intermediary Device, as specified in § 11.56(b).

<sup>2</sup> Wireless cable systems serving <5,000 subscribers are permitted to operate without an EAS encoder if they install an FCC-certified decoder.

<sup>3</sup> All wireless cable systems may comply with this requirement by providing a means to switch all programmed channels to a predesignated channel that carries the required audio and video EAS messages.

<sup>4</sup> The Video interrupt must cause all channels that carry programming to flash for the duration of the EAS emergency message. The audio alert must give the channel where the EAS messages are carried and be repeated for the duration of the EAS message. [*Note:* Programmed channels do not include channels used for the transmission of data services such as Internet.]

**Digital Cable Systems and Wireline Video Systems**

Digital cable systems and Wireline Video Systems must comply with the requirements in Table 4 below. Digital cable systems and Wireline Video Systems serving fewer than 5,000 subscribers from a headend must either provide the National level EAS message on all programmed channels including the required testing, or comply with the requirements in Table 4.

Table 4—Digital Cable System and Wireline Video System Equipment Deployment Requirements

| EAS equipment requirement | ≥5,000 subscribers | <5,000 subscribers |
|---|---|---|
| EAS decoder <sup>1</sup> | Y | Y |
| EAS encoder | Y | Y <sup>2</sup> |
| Audio and Video EAS Message on all channels <sup>3</sup> | Y | N |
| Video interrupt and audio alert message on all channels; <sup>4</sup> Audio and Video EAS message on at least one channel | N | Y |

<sup>1</sup> EAS Participants may comply with the obligations set forth in § 11.56 to decode and convert CAP-formatted messages into EAS Protocol-compliant messages by deploying an Intermediary Device, as specified in § 11.56(b).

<sup>2</sup> Digital cable systems and wireline video systems serving <5,000 subscribers are permitted to operate without an EAS encoder if they install an FCC-certified decoder.

<sup>3</sup> All digital cable systems and wireline video systems may comply with this requirement by providing a means to switch all programmed channels to a predesignated channel that carries the required audio and video EAS messages.

<sup>4</sup> The Video interrupt must cause all channels that carry programming to flash for the duration of the EAS emergency message. The audio alert must give the channel where the EAS messages are carried and be repeated for the duration of the EAS message. [*Note:* Programmed channels do not include channels used for the transmission of data services such as Internet access.]

SDARS and DBS

| EAS equipment requirement | SDARS | DBS |
|---|---|---|
| EAS decoder <sup>1</sup> | Y | Y |
| EAS encoder | Y | Y |
| Audio message on all channels <sup>2</sup> | Y | Y |
| Video message on all channels <sup>2</sup> | N/A | Y |

<sup>1</sup> EAS Participants may comply with the obligations set forth in § 11.56 to decode and convert CAP-formatted messages into EAS Protocol-compliant messages by deploying an Intermediary Device, as specified in § 11.56(b).

<sup>2</sup> All SDARS and DBS providers may comply with this requirement by providing a means to switch all programmed channels to a predesignated channel that carries the required audio and video EAS messages or by any other method that ensures that viewers of all channels receive the EAS message.

(b) Analog class D non-commercial educational FM stations as defined in § 73.506 of this chapter, digital class D non-commercial educational FM stations, analog LPFM stations as defined in §§ 73.811 and 73.853 of this chapter, digital LPFM stations, and LPTV stations as defined in § 74.701(b) of this chapter are not required to comply with § 11.32. Television broadcast translator stations, as defined in § 74.701(a) of this chapter, which entirely rebroadcast the programming of other broadcast televisions stations, are not required to comply with the requirements of this part. FM broadcast booster stations as defined in § 74.1201(f) of this chapter and FM translator stations as defined in § 74.1201(a) of this chapter which entirely rebroadcast the programming of other local FM broadcast stations are not required to comply with the requirements of this part. International broadcast stations as defined in § 73.701 of this chapter are not required to comply with the requirements of this part. Analog and digital broadcast stations that operate as satellites or repeaters of a hub station (or common studio or control point if there is no hub station) and rebroadcast 100 percent of the programming of the hub station (or common studio or control point) may satisfy the requirements of this part through the use of a single set of EAS equipment at the hub station (or common studio or control point) which complies with §§ 11.32 and 11.33.

(c) For purposes of the EAS, Broadband Radio Service (BRS) and Educational Broadband Service (EBS) stations operated as part of wireless cable systems in accordance with subpart M of part 27 of this chapter are defined as follows:

(1) A “wireless cable system” is a collection of channels in the BRS or EBS used to provide video programming services to subscribers. The channels may be licensed to or leased by the wireless cable system operator.

(2) A “wireless cable operator” is the entity that has acquired the right to use the channels of a wireless cable system for transmission of programming to subscribers.

(d) Local franchise authorities may use any EAS codes authorized by the FCC in any agreements.

(e) [Reserved]

[63 FR 29662, June 1, 1998, as amended at 65 FR 7639, Feb. 15, 2000; 65 FR 21657, Apr. 24, 2000; 65 FR 30001, May 10, 2000; 65 FR 34406, May 30, 2000; 67 FR 18506, Apr. 16, 2002; 69 FR 72031, Dec. 10, 2004; 70 FR 19315, Apr. 13, 2005; 70 FR 71031, Nov. 25, 2005; 71 FR 76220, Dec. 20, 2006; 72 FR 62132, Nov. 2, 2007; 77 FR 16699, Mar. 22, 2012; 89 FR 26792, Apr. 16, 2024; 91 FR 2872, Jan. 23, 2026; 91 FR 1404, Jan. 14, 2026]

### §§ 11.12-11.14 [Reserved]

### § 11.15 EAS Operating Handbook.

The EAS Operating Handbook states in summary form the actions to be taken by personnel at EAS Participant facilities upon receipt of an EAN, an EAT, tests, or State and Local Area alerts. It is issued by the FCC and contains instructions for the above situations. A copy of the Handbook must be located at normal duty positions or EAS equipment locations when an operator is required to be on duty and be immediately available to staff responsible for authenticating messages and initiating actions.

[70 FR 71033, Nov. 25, 2005]

### § 11.16 National Control Point Procedures.

The National Control Point Procedures are written instructions issued by the FCC to national level EAS control points. The procedures are divided into sections as follows:

(a) *National Level EAS Activation.* This section contains the activation and termination instructions for the National Emergency Message.

(b) *EAS Test Transmissions.* This section contains the instructions for testing the EAS at the National level.

[59 FR 67092, Dec. 28, 1994, as amended at 67 FR 18508, Apr. 16, 2002; 87 FR 67823, Nov. 10, 2022]

### § 11.18 EAS Designations.

(a) A Primary Entry Point (PEP) is a private or commercial radio broadcast station that cooperatively participates with FEMA to provide EAS alerts to the public. PEPs are the primary source of initial broadcast for a Presidential Alert. A PEP is equipped with back-up communications equipment and power generators designed to enable it to continue broadcasting information to the public during and after disasters of national significance. The National Public Warning System (formerly called the Primary Entry Point System) is a nationwide network of broadcast stations and satellite operators used to distribute EAS alerts formatted in the EAS Protocol. FEMA is responsible for designating broadcast stations as PEPs.

(b) A National Primary (NP) is an entity tasked with the primary responsibility of receiving the National Emergency Message from a PEP and delivering it to an individual state or portion of a state. In states without a PEP, the NP is responsible for receiving the National Emergency Message from an out-of-state PEP and transmitting it to the public and other EAS Participants in the state. Multiple entities may be charged with primary responsibility for delivering the National Emergency Message.

(c) A State Primary (SP) is an entity tasked with initiating the delivery of EAS alerts other than the National Emergency Message.

(d) A State Relay (SR) is an entity not otherwise designated that is charged with retransmitting EAS alerts for the purpose of being monitored by a Local Primary or Participating National. SRs must monitor or deliver EAS alerts as required by the State EAS Plan.

(e) A State Relay Network (SRN) is a network composed of State Relay (SR) sources, leased common carrier communications facilities, or any other available communication facilities. The network distributes State EAS messages originated by the Governor or designated official. In addition to EAS monitoring, satellites, microwave, FM subcarrier, or any other communications technology may be used to distribute State emergency messages.

(f) A Local Primary (LP) is an entity that serves as a monitoring assignment for other EAS Participants within the state. LP sources may be assigned numbers (e.g., LP-1, 2, 3) and are relied on as monitoring sources by other EAS Participants in the Local Area. An LP may monitor any other station, including another LP, as set forth in the State EAS Plan, so long as doing so avoids creating a single point of failure in the alert distribution hierarchy.

(g) A Participating National (PN) is an EAS Participant that transmits national, state, or Local Area EAS messages, and is not otherwise designated within the State EAS Plan. PNs monitor LPs or other sources as set forth in the State EAS Plan.

[87 FR 67823, Nov. 10, 2022]

### § 11.20 [Reserved]

### § 11.21 State EAS Plans.

(a) EAS plans contain guidelines which must be followed by EAS Participants' personnel, emergency officials, and National Weather Service (NWS) personnel to activate the EAS. The plans include the EAS header codes and messages that will be transmitted by key EAS sources (NP, LP, SP and SR). State and local plans contain unique methods of EAS message distribution such as the use of the Radio Broadcast Data System (RBDS). The plans also include information on actions taken by EAS Participants, in coordination with state and local governments, to ensure timely access to EAS alert content by non-English speaking populations. The plans must be reviewed and approved by the Chief, Public Safety and Homeland Security Bureau (Bureau), prior to implementation to ensure that they are consistent with national plans, FCC regulations, and EAS operation. The plans are administered by State Emergency Communications Committees (SECC). The Commission encourages the chief executive of each State to establish an SECC if their State does not have an SECC, and if the State has an SECC, to review the composition and governance of the SECC. The Bureau will review and approve plans, including annual updated plans, within 60 days of receipt, provided that no defects are found requiring the plan to be returned to the SECC for correction and resubmission. If a plan submitted for approval is found defective, the SECC will be notified of the required corrections, and the corrected plan may be resubmitted for approval, thus starting the 60-day review and approval period anew. The approval dates of State EAS Plans will be listed on the Commission's website.

(b) State EAS Plans contain guidelines that must be followed by EAS Participants' personnel, emergency officials, and National Weather Service (NWS) personnel to activate the EAS. The Plans include information on actions taken by EAS Participants, in coordination with state and local governments, to ensure timely access to EAS alert content by non-English speaking populations. State EAS Plans must be updated on an annual basis. State EAS Plans must include the following elements:

(1) A list of the EAS header codes and messages that will be transmitted by key EAS sources (NP, LP, SP, and SR);

(2) Procedures for state emergency management officials, the National Weather Service, and EAS Participant personnel to transmit emergency information to the public during an emergency via the EAS, including the extent to which the state's dissemination strategy for state and local emergency alerts differs from its strategy for the National Emergency Message;

(3) Procedures for state and local activations of the EAS, including a list of all authorized entities participating in the State or Local Area EAS;

(4) A monitoring assignment matrix, in computer readable form, clearly showing monitoring assignments and the specific primary and backup path for the National Emergency Message (EAN) from the NPWS to all key EAS sources (using the uniform designations specified in § 11.18) and to each station in the plan, organized by operational areas within the state. If a state's emergency alert system is capable of initiating EAS messages formatted in the Common Alerting Protocol (CAP), its EAS State Plan must include specific and detailed information describing how such messages will be aggregated and distributed to EAS Participants within the state, including the monitoring requirements associated with distributing such messages; State EAS Plans must indicate whether any of the EAS monitoring sources in the monitoring assignment matrix are primary stations adopting program originating boosters and, if so, whether the boosters will simulcast the primary station or remain off-air during periods when they are not originating programming;

(5) State procedures for conducting special EAS tests and Required Monthly Tests (RMTs);

(6) A list of satellite-based communications resources that are used as alternate monitoring assignments and present a reliable source of EAS messages; and

(7) The SECC governance structure utilized by the state in order to organize state and local resources to ensure the efficient and effective delivery of a National Emergency Message, including the duties of the SECC, the membership selection process utilized by the SECC, and the administrative structure of the SECC.

(8) Certification by the SECC Chairperson or Vice-Chairperson that the SECC met (in person, via teleconference, or via other methods of conducting virtual meetings) at least once in the twelve months prior to submitting the annual updated plan to review and update the plan.

[72 FR 62134, Nov. 2, 2007, as amended at 77 FR 16700, Mar. 22, 2012; 80 FR 37174, June 30, 2015; 81 FR 27351, May 6, 2016; 83 FR 37759, Aug. 2, 2018; 86 FR 46791, Aug. 20, 2021; 87 FR 34215, June 6, 2022; 87 FR 67823, Nov. 10, 2022; 89 FR 100876, Dec. 13, 2024; 91 FR 1404, Jan. 14, 2026]

## Subpart B—Equipment Requirements

### § 11.31 EAS protocol.

(a) The EAS uses a four part message for an emergency activation of the EAS. The four parts are: Preamble and EAS Header Codes; audio Attention Signal; message; and, Preamble and EAS End Of Message (EOM) Codes.

(1) The Preamble and EAS Codes must use Audio Frequency Shift Keying at a rate of 520.83 bits per second to transmit the codes. Mark frequency is 2083.3 Hz and space frequency is 1562.5 Hz. Mark and space time must be 1.92 milliseconds. Characters are ASCII seven bit characters as defined in ANSI X3.4-1977 ending with an eighth null bit (either 0 or 1) to constitute a full eight-bit byte.

(2) The Attention Signal must be made up of the fundamental frequencies of 853 and 960 Hz. The two tones must be transmitted simultaneously. The Attention Signal must be transmitted after the EAS header codes.

(3) The message may be audio, video or text.

(b) The ASCII dash and plus symbols are required and may not be used for any other purpose. Unused characters must be ASCII space characters. FM or TV call signs must use a slash ASCII character number 47 (/) in lieu of a dash.

(c) The EAS protocol, including any codes, must not be amended, extended or abridged without FCC authorization. The EAS protocol and message format are specified in the following representation.

Examples are provided in FCC Public Notices.

[PREAMBLE]ZCZC-ORG-EEE-PSSCCC + TTTT-JJJHHMM-LLLLLLLL-(one second pause)

[PREAMBLE]ZCZC-ORG-EEE-PSSCCC + TTTTpJJJHHMM-LLLLLLLL-(one second pause)

[PREAMBLE]ZCZC-ORG-EEE-PSSCCC + TTTT-JJJHHMM-LLLLLLLL-(at least a one second pause)

(transmission of 8 to 25 seconds of Attention Signal)

(transmission of audio, video or text messages)

(at least a one second pause)

[PREAMBLE]NNNN (one second pause)

[PREAMBLE]NNNN (one second pause)

[PREAMBLE]NNNN (at least one second pause)

[PREAMBLE] This is a consecutive string of bits (sixteen bytes of AB hexadecimal [8 bit byte 10101011]) sent to clear the system, set AGC and set asynchronous decoder clocking cycles. The preamble must be transmitted before each header and End of Message code.

ZCZC—This is the identifier, sent as ASCII characters ZCZC to indicate the start of ASCII code.

ORG—This is the Originator code and indicates who originally initiated the activation of the EAS. These codes are specified in paragraph (d) of this section.

EEE—This is the Event code and indicates the nature of the EAS activation. The codes are specified in paragraph (e) of this section. The Event codes must be compatible with the codes used by the NWS Weather Radio Specific Area Message Encoder (WRSAME).

PSSCCC—This is the Location code and indicates the geographic area affected by the EAS alert. There may be 31 Location codes in an EAS alert. The Location code uses the codes described in the American National Standards Institute (ANSI) standard, ANSI INCITS 31-2009 (“Information technology—Codes for the Identification of Counties and Equivalent Areas of the United States, Puerto Rico, and the Insular Areas”). Each state is assigned an SS number as specified in paragraph (f) of this section. Each county and some cities are assigned a CCC number. A CCC number of 000 refers to an entire State or Territory. P defines county subdivisions as follows: 0 = all or an unspecified portion of a county, 1 = Northwest, 2 = North, 3 = Northeast, 4 = West, 5 = Central, 6 = East, 7 = Southwest, 8 = South, 9 = Southeast. Other numbers may be designated later for special applications. The use of county subdivisions will probably be rare and generally for oddly shaped or unusually large counties. Any subdivisions must be defined and agreed to by the local officials prior to use.

\+ TTTT—This indicates the valid time period of a message in 15 minute segments up to one hour and then in 30 minute segments beyond one hour; *i.e.*, + 0015, + 0030, + 0045, + 0100, + 0430 and + 0600.

JJJHHMM—This is the day in Julian Calendar days (JJJ) of the year and the time in hours and minutes (HHMM) when the message was initially released by the originator using 24 hour Universal Coordinated Time (UTC).

LLLLLLLL—This is the identification of the EAS Participant, NWS office, etc., transmitting or retransmitting the message. These codes will be automatically affixed to all outgoing messages by the EAS encoder.

NNNN—This is the End of Message (EOM) code sent as a string of four ASCII N characters.

(d)(1) The only originator codes are:

Table 1 to Paragraph **(d)(1)**

| Originator | ORG code |
|---|---|
| EAS Participant | EAS |
| Civil authorities | CIV |
| National Weather Service | WXR |
| United States Government | PEP |

(2) [Reserved]

(e) The following Event (EEE) codes are presently authorized:

Table 2 to Paragraph **(e)**

| Nature of activation | Event codes |
|---|---|
| National Codes (Required): |  |
| Emergency Action Notification (National only) | EAN. |
| National Information Center | NIC. |
| National Periodic Test | NPT. |
| Required Monthly Test | RMT. |
| Required Weekly Test | RWT. |
| State and Local Codes (Optional): |  |
| Administrative Message | ADR. |
| Avalanche Warning | AVW. |
| Avalanche Watch | AVA. |
| Blizzard Warning | BZW. |
| Blue Alert | BLU. |
| Child Abduction Emergency | CAE. |
| Civil Danger Warning | CDW. |
| Civil Emergency Message | CEM. |
| Coastal Flood Warning | CFW. |
| Coastal Flood Watch | CFA. |
| Dust Storm Warning | DSW. |
| Earthquake Warning | EQW. |
| Evacuation Immediate | EVI. |
| Extreme Wind Warning | EWW. |
| Fire Warning | FRW. |
| Flash Flood Warning | FFW. |
| Flash Flood Watch | FFA. |
| Flash Flood Statement | FFS. |
| Flood Warning | FLW. |
| Flood Watch | FLA. |
| Flood Statement | FLS. |
| Hazardous Materials Warning | HMW. |
| High Wind Warning | HWW. |
| High Wind Watch | HWA. |
| Hurricane Warning | HUW. |
| Hurricane Watch | HUA. |
| Hurricane Statement | HLS. |
| Law Enforcement Warning | LEW. |
| Local Area Emergency | LAE. |
| Missing and Endangered Persons | MEP. |
| Network Message Notification | NMN. |
| 911 Telephone Outage Emergency | TOE. |
| Nuclear Power Plant Warning | NUW. |
| Practice/Demo Warning | DMO. |
| Radiological Hazard Warning | RHW. |
| Severe Thunderstorm Warning | SVR. |
| Severe Thunderstorm Watch | SVA. |
| Severe Weather Statement | SVS. |
| Shelter in Place Warning | SPW. |
| Special Marine Warning | SMW. |
| Special Weather Statement | SPS. |
| Storm Surge Watch | SSA. |
| Storm Surge Warning | SSW. |
| Tornado Warning | TOR. |
| Tornado Watch | TOA. |
| Tropical Storm Warning | TRW. |
| Tropical Storm Watch | TRA. |
| Tsunami Warning | TSW. |
| Tsunami Watch | TSA. |
| Volcano Warning | VOW. |
| Winter Storm Warning | WSW. |
| Winter Storm Watch | WSA. |

(f) The All U.S., State, Territory and Offshore (Marine Area) ANSI number codes (SS) are as follows. County ANSI numbers (CCC) are contained in the State EAS Mapbook.

Table 3 to Paragraph **(f)**

|  | ANSI No. |
|---|---|
| All U.S | 00 |
| State: |  |
| AL | 01 |
| AK | 02 |
| AZ | 04 |
| AR | 05 |
| CA | 06 |
| CO | 08 |
| CT | 09 |
| DE | 10 |
| DC | 11 |
| FL | 12 |
| GA | 13 |
| HI | 15 |
| ID | 16 |
| IL | 17 |
| IN | 18 |
| IA | 19 |
| KS | 20 |
| KY | 21 |
| LA | 22 |
| ME | 23 |
| MD | 24 |
| MA | 25 |
| MI | 26 |
| MN | 27 |
| MS | 28 |
| MO | 29 |
| MT | 30 |
| NE | 31 |
| NV | 32 |
| NH | 33 |
| NJ | 34 |
| NM | 35 |
| NY | 36 |
| NC | 37 |
| ND | 38 |
| OH | 39 |
| OK | 40 |
| OR | 41 |
| PA | 42 |
| RI | 44 |
| SC | 45 |
| SD | 46 |
| TN | 47 |
| TX | 48 |
| UT | 49 |
| VT | 50 |
| VA | 51 |
| WA | 53 |
| WV | 54 |
| WI | 55 |
| WY | 56 |
| Terr.: |  |
| AS | 60 |
| FM | 64 |
| GU | 66 |
| MH | 68 |
| PR | 72 |
| PW | 70 |
| UM | 74 |
| VI | 78 |
| Offshore (Marine Areas) <sup>1</sup> |  |
| Eastern North Pacific Ocean, and along U.S. West Coast from Canadian border to Mexican border | 57 |
| North Pacific Ocean near Alaska, and along Alaska coastline, including the Bering Sea and the Gulf of Alaska | 58 |
| Central Pacific Ocean, including Hawaiian waters | 59 |
| South Central Pacific Ocean, including American Samoa waters | 61 |
| Western Pacific Ocean, including Mariana Island waters | 65 |
| Western North Atlantic Ocean, and along U.S. East Coast, from Canadian border south to Currituck Beach Light, N.C | 73 |
| Western North Atlantic Ocean, and along U.S. East Coast, south of Currituck Beach Light, NC, following the coastline to Ocean Reef, FL, including the Caribbean | 75 |
| Gulf of Mexico, and along the U.S. Gulf Coast from the Mexican border to Ocean Reef, FL | 77 |
| Lake Superior | 91 |
| Lake Michigan | 92 |
| Lake Huron | 93 |
| Lake St. Clair | 94 |
| Lake Erie | 96 |
| Lake Ontario | 97 |
| St. Lawrence River above St. Regis | 98 |

<sup>1</sup> The numbers assigned to the offshore marine areas listed in this table are not described under the ANSI standard, but rather are numeric codes that were assigned by the National Weather Service.

[59 FR 67092, Dec. 28, 1994, as amended at 60 FR 55999, Nov. 6, 1995; 61 FR 54952, Oct. 23, 1996; 63 FR 29663, June 1, 1998; 67 FR 18508, Apr. 16, 2002; 67 FR 77174, Dec. 17, 2002; 69 FR 72031, Dec. 10, 2004; 70 FR 71033, Nov. 25, 2005; 77 FR 16701, Mar. 22, 2012; 80 FR 37174, June 30, 2015; 81 FR 53043, Aug. 11, 2016; 83 FR 2563, Jan. 18, 2018; 87 FR 67823, Nov. 10, 2022; 89 FR 72737, Sept. 6, 2024; 91 FR 1404, Jan. 14, 2026]

### § 11.32 EAS Encoder.

(a) EAS Encoders must at a minimum be capable of encoding the EAS protocol described in § 11.31 and providing the EAS code transmission requirements described in § 11.51. EAS encoders must additionally provide the following minimum specifications:

(1) *Encoder programming.* Access to encoder programming shall be protected by a lock or other security measures and be configured so that authorized personnel can readily select and program the EAS Encoder with Originator, Event and Location codes for either manual or automatic operation.

(2) *Inputs.* The encoder shall have at least one input port used for audio messages and at least one input port used for data messages.

(3) *Outputs.* The encoder shall have at least one audio output port and at least one data output port.

(4) *Calibration.* EAS Encoders must provide a means to comply with the modulation levels required in § 11.51(f).

(5) Day-Hour-Minute and Identification Stamps. The encoder shall affix the JJJHHMM and LLLLLLLL codes automatically to all initial messages.

(6) *Program Data Retention.* Program data and codes shall be retained even with the power removed.

(7) *Indicator.* An aural or visible means that it activated when the Preamble is sent and deactivated at the End of Message code.

(8) *Spurious Response.* All frequency components outside 200 to 4000 Hz shall be attenuated by 40 dB or more with respect to the output levels of the mark or space frequencies.

(9) *Attention Signal generator.* The encoder must provide an attention signal that complies with the following:

(i) *Tone Frequencies.* The audio tones shall have fundamental frequencies of 853 and 960 Hz and not vary over ±0.5 Hz.

(ii) *Harmonic Distortion.* The total harmonic distortion of each of the audio tones may not exceed 5% at the encoder output terminals.

(iii) *Minimum Level of Output.* The encoder shall have an output level capability of at least + 8 dBm into a 600 Ohm load impedance at each audio tone. A means shall be provided to permit individual activation of the two tones for calibration of associated systems.

(iv) *Time Period for Transmission of Tones.* The encoder shall have timing circuitry that automatically generates the two tones simultaneously for a time period of 8 seconds.

(v) *Inadvertent activation.* The switch used for initiating the automatic generation of the simultaneous tones shall be protected to prevent accidental operation.

(vi) *Indicator Display.* The encoder shall be provided with a visual and/or aural indicator which clearly shows that the Attention Signal is activated.

(b) *Operating Temperature and Humidity.* Encoders shall have the ability to operate with the above specifications within an ambient temperature range of 0 to + 50 degrees C and a range of relative humidity of up to 95%.

(c) *Primary Supply Voltage Variation.* Encoders shall be capable of complying with the requirements of this section during a variation in primary supply voltage of 85 percent to 115 percent of its rated value.

(d) *Testing Encoder Units.* Encoders not covered by § 11.34(e) of this part shall be tested in a 10 V/m minimum RF field at an AM broadcast frequency and a 0.5 V/m minimum RF field at an FM or TV broadcast frequency to simulate actual working conditions.

[59 FR 67092, Dec. 28, 1994, as amended at 77 FR 16703, Mar. 22, 2012]

### § 11.33 EAS Decoder.

(a) An EAS Decoder must at a minimum be capable of providing the EAS monitoring functions described in § 11.52, decoding EAS messages formatted in accordance with the EAS Protocol described in § 11.31, and converting Common Alerting Protocol (CAP)-formatted EAS messages into EAS alert messages that comply with the EAS Protocol, in accordance with § 11.56(a)(2), with the exception that the CAP-related monitoring and conversion requirements set forth in §§ 11.52(d)(2) and 11.56(a)(2) can be satisfied via an Intermediary Device, as specified in § 11.56(b), provided that all other requirements set forth in this part are met. An EAS Decoder also must be capable of the following minimum specifications:

(1) *Inputs.* Decoders must have the capability to receive at least two audio inputs from EAS monitoring assignments, and at least one data input. The data input(s) may be used to monitor other communications modes such as Radio Broadcast Data System (RBDS), NWR, satellite, public switched telephone network, or any other source that uses the EAS protocol.

(2) *Valid codes.* There must be a means to determine if valid EAS header codes are received and to determine if preselected header codes are received.

(3) *Storage.* Decoders must provide the means to:

(i) Record and store, either internally or externally, at least two minutes of audio or text messages. A decoder manufactured without an internal means to record and store audio or text must be equipped with a means (such as an audio or digital jack connection) to couple to an external recording and storing device.

(ii) Store at least ten preselected event and originator header codes, in addition to the seven mandatory event/originator codes for tests and national activations, and store any preselected location codes for comparison with incoming header codes. A non-preselected header code that is manually transmitted must be stored for comparison with later incoming header codes. The header codes of the last ten received valid messages which still have valid time periods must be stored for comparison with the incoming valid header codes for later messages. These last received header codes will be deleted from storage as their valid time periods expire.

(4) *Display and logging.* For received alert messages formatted in both the EAS Protocol and Common Alerting Protocol, a visual message shall be developed from any valid header codes for tests and national activations and any preselected header codes received. The message shall at a minimum include the Originator, Event, Location, the valid time period of the message and the local time the message was transmitted. The message shall be in the primary language of the EAS Participant and be fully displayed on the decoder and readable in normal light and darkness. The visual message developed from received alert messages formatted in the Common Alerting Protocol must conform to the requirements in §§ 11.51(d), (g)(3), (h)(3), and (j)(2) of this part. All existing and new models of EAS decoders manufactured after August 1, 2003 must provide a means to permit the selective display and logging of EAS messages containing header codes for state and local EAS events. Effective May 16, 2002, analog radio and television broadcast stations, analog cable systems and wireless cable systems may upgrade their decoders on an optional basis to include a selective display and logging capability for EAS messages containing header codes for state and local events. EAS Participants that install or replace their decoders after February 1, 2004 must install decoders that provide a means to permit the selective display and logging of EAS messages containing header codes for state and local EAS events.

(5) *Indicators.* EAS decoders must have a distinct and separate aural or visible means to indicate when any of the following conditions occurs:

(i) Any valid EAS header codes are received as specified in § 11.33(a)(10).

(ii) Preprogrammed header codes, such as those selected in accordance with § 11.52(d)(2) are received.

(iii) A signal is present at each audio input that is specified in § 11.33(a)(1).

(6) *Program Data Retention.* The program data must be retained even with power removed.

(7) *Outputs.* Decoders shall have at least one data port where received valid EAS header codes and received preselected header codes are available, at least one audio port that is capable of monitoring each decoder audio input, and an internal speaker to enable personnel to hear audio from each input.

(8) *Decoder Programming.* Access to decoder programming shall be protected by a lock or other security measures and be configured so that authorized personnel can readily select and program the EAS Decoder with preselected Originator, Event and Location codes for either manual or automatic operation.

(9) *Reset.* There shall be a method to automatically or manually reset the decoder to the normal monitoring condition. Operators shall be able to select a time interval, not less than two minutes, in which the decoder would automatically reset if it received an EAS header code but not an end-of-message (EOM) code. Messages received with the EAN Event codes shall disable the reset function so that lengthy audio messages can be handled. The last message received with valid header codes shall be displayed as required by paragraph (a)(4) of this section before the decoder is reset.

(10) *Message Validity.* An EAS Decoder must provide error detection and validation of the header codes of each message to ascertain if the message is valid. Header code comparisons may be accomplished through the use of a bit-by-bit compare or any other error detection and validation protocol. A header code must only be considered valid when two of the three headers match exactly; the Origination Date/Time field (JJJHHMM) is not more than 15 minutes in the future and the expiration time (Origination Date/Time plus Valid Time TTTT) is in the future (*i.e.,* current time at the EAS equipment when the alert is received is between origination time minus 15 minutes and expiration time). Duplicate messages must not be relayed automatically.

(11) A header code with the EAN Event code specified in § 11.31(c) that is received through any of the audio or data inputs must override all other messages.

(b) Decoders shall be capable of operation within the tolerances specified in this section as well as those in § 11.32 (b), (c) and (d).

[59 FR 67092, Dec. 28, 1994, as amended at 60 FR 55999, Nov. 6, 1995; 67 FR 18510, Apr. 16, 2002; 70 FR 71033, Nov. 25, 2005; 77 FR 16703, Mar. 22, 2012; 83 FR 39620, Aug. 10, 2018]

### § 11.34 Acceptability of the equipment.

(a) An EAS Encoder used for generating the EAS codes and the Attention Signal must be Certified in accordance with the procedures in part 2, subpart J, of this chapter. The data and information submitted must show the capability of the equipment to meet the requirements of this part as well as the requirements contained in part 15 of this chapter for digital devices.

(b) Decoders used for the detection of the EAS codes and receiving the Attention Signal must be Certified in accordance with the procedures in part 2, subpart J, of this chapter. The data and information submitted must show the capability of the equipment to meet the requirements of this part as well as the requirements contained in part 15 of this chapter for digital devices.

(c) The functions of the EAS decoder, Attention Signal generator and receiver, and the EAS encoder specified in §§ 11.31, 11.32 and 11.33 may be combined and Certified as a single unit provided that the unit complies with all specifications in this rule section.

(d) Manufacturers must include instructions and information on how to install, operate and program an EAS Encoder, EAS Decoder, or combined unit and a list of all State and county ANSI numbers with each unit sold or marketed in the U.S.

(e) Waiver requests of the Certification requirements for EAS Encoders or EAS Decoders which are constructed for use by an EAS Participant, but are not offered for sale will be considered on an individual basis in accordance with part 1, subpart G, of this chapter.

(f) Modifications to existing authorized EAS decoders, encoders or combined units necessary to implement the new EAS codes specified in § 11.31 and to implement the selective displaying and logging feature specified in § 11.33(a)(4) will be considered Class I permissive changes that do not require a new application for and grant of equipment certification under part 2, subpart J of this chapter.

(g) [Reserved]

[59 FR 67092, Dec. 28, 1994, as amended at 60 FR 56000, Nov. 6, 1995; 67 FR 18510, Apr. 16, 2002; 70 FR 71034, Nov. 25, 2005; 77 FR 16703, Mar. 22, 2012; 91 FR 1404, Jan. 14, 2026]

### § 11.35 Equipment operational readiness.

(a) EAS Participants are responsible for ensuring that EAS Encoders, EAS Decoders, Attention Signal generating and receiving equipment, and Intermediate Devices used as part of the EAS to decode and/or encode messages formatted in the EAS Protocol and/or the Common Alerting Protocol are installed so that the monitoring and transmitting functions are available during the times the stations and systems are in operation. Additionally, EAS Participants must determine the cause of any failure to receive the required tests or activations specified in § 11.61(a)(1) and (2). Appropriate entries indicating reasons why any tests were not received must be made in the broadcast station log as specified in §§ 73.1820 and 73.1840 of this chapter for all broadcast streams and cable system records as specified in §§ 76.1700, 76.1708, and 76.1711 of this chapter. All other EAS Participants must also keep records indicating reasons why any tests were not received and these records must be retained for two years, maintained at the EAS Participant's headquarters, and made available for public inspection upon reasonable request.

(b) If an EAS Encoder, EAS Decoder or Intermediary Device used as part of the EAS to decode and/or encode messages formatted in the EAS Protocol and/or the Common Alerting Protocol becomes defective, the EAS Participant may operate without the defective equipment pending its repair or replacement for 60 days without further FCC authority. Entries shall be made in the broadcast station log, cable system records, and records of other EAS Participants, as specified in paragraph (a) of this section, showing the date and time the equipment was removed and restored to service. For personnel training purposes, the required monthly test script must still be transmitted even though the equipment for generating the EAS message codes, Attention Signal and EOM code is not functioning.

(c) If repair or replacement of defective equipment is not completed within 60 days, an informal request shall be submitted to the Regional Director of the FCC field office serving the area in which the EAS Participant is located, or in the case of DBS and SDARS providers to the Regional Director of the FCC field office serving the area where their headquarters is located, for additional time to repair the defective equipment. This request must explain what steps have been taken to repair or replace the defective equipment, the alternative procedures being used while the defective equipment is out of service, and when the defective equipment will be repaired or replaced.

(d) EAS Participants shall employ the following security controls with respect to EAS equipment, studio transmitter link equipment, and any remotely managed equipment that routes, processes, or inserts content into the transmission of the EAS Participant's programming:

(1) Prior to any use to broadcast to the public, EAS Participants shall change any default password, use strong passwords, and change any password if the EAS Participant has reason to believe that the password has been compromised.

(i) A strong password is any password that has a minimum of 15 characters and does not use dictionary words. Instead of using a strong password, EAS Participants may use alternative authentication measures, such as look-up secrets, out-of-band devices, single- or multi-factor one-time password devices, or single- or multi-factor cryptographic authentication, that are reasonably sufficient to mitigate the risk of unauthorized access.

(ii) Passwords employed to comply with this requirement shall not be reused for the EAS Participant's other accounts, equipment, applications, or services.

(2) Install security patches and security-related software and firmware updates issued by equipment manufacturers promptly after those patches or upgrades become available. Security patches and security-related software and firmware updates issued by equipment manufacturers may be tested before they are installed, provided that the testing begins promptly and is completed in a timeframe that is consistent with industry best practices; and

(3) Use a network firewall or comparable network segmentation practice that limits remote management access to authorized devices and authorized users.

[70 FR 71034, Nov. 25, 2005, as amended at 77 FR 16704, Mar. 22, 2012; 80 FR 53750, Sept. 8, 2015; 91 FR 48300, July 31, 2026]

## Subpart C—Organization

### § 11.41 Participation in EAS.

All EAS Participants specified in § 11.11 are categorized as Participating National (PN) sources, and must have immediate access to an EAS Operating Handbook.

[77 FR 16704, Mar. 22, 2012]

### § 11.42 [Reserved]

### § 11.43 [Reserved]

### § 11.44 Alert repetition.

An alert originator may “repeat” an alert by releasing the alert anew—*i.e.,* re-originating the alert—at least one minute subsequent to the time the message was initially released by the originator, as reflected in the repeat alert's JJJHHMM header code. Because alerts take time to activate across the EAS alert distribution chain, alert originators should consider an interval between the original and re-originated alert that is long enough to account for this process. If the re-originated alert is intended to reflect a valid time period consistent with the original, the valid time period code (the +TTTT header code identified in § 11.31(c)) set for the re-originated alert should be adjusted to account for the elapsed time between the original and re-originated alerts. Alert originators should be aware that repeating alerts routinely may cause alert fatigue among the public.

[86 FR 46791, Aug. 20, 2021]

### § 11.45 Prohibition of false or deceptive EAS transmissions.

(a) No person may transmit or cause to transmit the EAS codes or Attention Signal, or a recording or simulation thereof, in any circumstance other than in an actual National, State or Local Area emergency or authorized test of the EAS; or as specified in §§ 10.520(d), 11.46, and 11.61 of this chapter.

(b) No later than twenty-four (24) hours of an EAS Participant's discovery (*i.e.,* actual knowledge) that it has transmitted or otherwise sent a false alert to the public, the EAS Participant shall send an email to the Commission at the FCC Ops Center at *FCCOPS@fcc.gov,* informing the Commission of the event and of any details that the EAS Participant may have concerning the event.

(c) If the Administrator of the Federal Emergency Management Agency or a State, local, Tribal, or territorial government entity becomes aware of transmission of an EAS false alert to the public, they are encouraged to send an email to the Commission at the FCC Ops Center at *FCCOPS@fcc.gov,* informing the Commission of the event and of any details that they may have concerning the event.

[83 FR 39621, Aug. 10, 2018, as amended at 86 FR 46791, Aug. 20, 2021; 87 FR 34215, June 6, 2022]

### § 11.46 EAS public service announcements.

EAS Participants may use the EAS Attention Signal and a simulation of the EAS codes as provided by FEMA in EAS Public Service Announcements (PSAs) (including commercially-sponsored announcements, infomercials, or programs) provided by federal, state, and local government entities, or non-governmental organizations, to raise public awareness about emergency alerting. This usage is only permitted if the PSA is presented in a non-misleading and technically harmless manner, including with the explicit statement that the Attention Signal and EAS code simulation are being used in the context of a PSA for the purpose of educating the viewing or listening public about emergency alerting.

[83 FR 39621, Aug. 10, 2018]

### § 11.47 [Reserved]

## Subpart D—Emergency Operations

### § 11.51 EAS code and Attention Signal Transmission requirements.

(a) Analog and digital broadcast stations must transmit, either automatically or manually, national level EAS messages and required tests by sending the EAS header codes, Attention Signal, emergency message and End of Message (EOM) codes using the EAS Protocol. The Attention Signal must precede any emergency audio message.

(b) When relaying EAS messages, EAS Participants may transmit only the EAS header codes and the EOM code without the Attention Signal and emergency message for State and local emergencies. Pauses in video programming before EAS message transmission should not cause television receivers to mute EAS audio messages. No Attention Signal is required for EAS messages that do not contain audio programming, such as a Required Weekly Test.

(c) All analog and digital radio and television stations shall transmit EAS messages in the main audio channel. All DAB stations shall also transmit EAS messages on all audio streams. All DTV broadcast stations shall also transmit EAS messages on all program streams.

(d) Analog and digital television broadcast stations, analog cable systems, digital cable systems, wireless cable systems, wireline video systems, and DBS providers shall transmit a visual message containing the Originator, Event, and Location and the valid time period of an EAS message. Visual messages derived from CAP-formatted EAS messages shall contain the Originator, Event, Location and the valid time period of the message and shall be constructed in accordance with § 3.6 of the “ECIG Recommendations for a CAP EAS Implementation Guide, Version 1.0” (May 17, 2010).

(1) The visual message portion of an EAS alert, whether video crawl or block text, must be displayed:

(i) At the top of the television screen or where it will not interfere with other visual messages

(ii) In a manner (*i.e.,* font size, color, contrast, location, and speed) that is readily readable and understandable,

(iii) In a manner that does not contain overlapping lines of EAS text or extend beyond the viewable display (except for video crawls that intentionally scroll on and off of the screen), and

(iv) In full at least once during any EAS message.

(2) The audio portion of an EAS message must play in full at least once during any EAS message.

(3) On and after December 12, 2023,

(i) The portion of the required visual message corresponding with the Originator Code shall use the term in the first column in the table in § 11.31(d) corresponding to the ORG code in the second column of that table.

(ii) The portion of the required visual message corresponding with the Event Code shall use the term in the first column in the table in § 11.31(e) corresponding to the Event code in the second column of that table, except as set forth in paragraphs (d)(3)(iii) and (d)(5) of this section.

(iii) Notwithstanding paragraphs (d)(3)(i) and (ii) of this section, if the header codes of the received EAS message specify the NPT Event code and the “All U.S.” location code, and if the received EAS message is formatted in the EAS protocol, then the required visual message shall consist of the following text instead of replicating the terms of the Originator, Event, and Location codes: “This is a nationwide test of the Emergency Alert System, issued by the Federal Emergency Management Agency, covering the United States from [time] until [time]. This is only a test. No action is required by the public.” The “from [time] until [time]” portion of the text required in the preceding sentence shall be determined from the alert's release date/time and valid time period header codes specified at § 11.31(c).

(4) Prior to December 12, 2023, the required visual message shall either conform to paragraph (d)(3) or, in the alternative, shall display—

(i) The term “Emergency Action Notification” as the portion of the visual message corresponding to the EAN Event code if the header codes of the received EAS message specify the EAN Event code.

(ii) The term “National Periodic Test” as the portion of the visual message corresponding to the NPT Event code if the header codes of the received EAS message specify the NPT Event code.

(iii) The term “Primary Entry Point” as the portion of the visual message corresponding to the PEP Originator code if the header codes of the received EAS message specify the PEP Originator code.

(5) If the EAS Participant is an analog or digital cable system subject to paragraphs (g) or (h) of this section, then—

(i) If, with respect to a particular subscriber, the portion of the required visual message corresponding to the EAN event code can be altered by means of software upgrades or other changes that do not require replacement of the subscriber's navigation device, then, prior to March 12, 2024, the portion of the required visual message displayed to the subscriber corresponding to the EAN Event code shall comply with either paragraph (d)(3)(ii) or (d)(4)(i) of this section; after that date, the portion of the required visual message displayed to the subscriber corresponding to the EAN Event code shall comply with paragraph (d)(3)(ii) of this section.

(ii) If, with respect to a particular subscriber, no alterations to the portion of the required visual message corresponding to the EAN event code can be implemented unless the subscriber's navigation device is replaced with a device that is capable of displaying the visual message corresponding to the EAN event code as set forth in paragraph (d)(3)(ii) of this section then, prior to December 12, 2028 or the date when the subscriber's navigation device is replaced, whichever occurs earliest—

(A) The portion of the required visual message displayed to the subscriber corresponding to the EAN Event code shall comply with either paragraph (d)(3)(ii) or paragraph (d)(4)(i) of this section; thereafter, the portion of the required visual message displayed to the subscriber corresponding to the EAN Event code shall comply with paragraph (d)(3)(ii) of this section.

(B) If the operator of the cable system makes the navigation device available to the subscriber as “associated equipment” in connection with a cable service, as the term “associated equipment” is used in part 76, subpart N of this chapter, and a subscriber who is deaf or hard of hearing requests that the cable system operator provide a navigation device that is capable of displaying a visual message that complies with paragraph (d)(1) of this section, to replace a navigation device that lacks such capability, then the cable system operator shall provide and, if necessary, install such replacement navigation device within a reasonable period of time, to the same extent required and on the same terms and conditions as set forth at § 79.108 of this chapter. This paragraph (d)(5)(ii)(B) applies only to subscribers who state that they are deaf or hard of hearing or a household member who is deaf or hard of hearing.

(iii) Prior to December 12, 2028, the cable system operator must prominently display on its website information regarding the availability of replacement navigation devices to eligible subscribers as set forth in paragraph (d)(5)(ii)(B) of this section, in the same manner as provided at § 79.108(d)(2) of this chapter.

(iv) For purposes of this paragraph (d)(5), the term “navigation device” means equipment that is located at a subscriber's premises and satisfies the definition of “navigation device” in § 76.1200(c) of this chapter.

(e) Analog class D non-commercial educational FM stations as defined in § 73.506 of this chapter, digital class D non-commercial educational FM stations, analog Low Power FM (LPFM) stations as defined in §§ 73.811 and 73.853 of this chapter, digital LPFM stations, and LPTV stations as defined in § 74.701(b) of this chapter are not required to have equipment capable of generating the EAS codes and Attention Signal specified in § 11.31.

(f) Analog and digital broadcast station equipment generating the EAS codes and the Attention Signal shall modulate a broadcast station transmitter so that the signal broadcast to other EAS Participants alerts them that the EAS is being activated or tested at the National, State or Local Area level. The minimum level of modulation for EAS codes, measured at peak modulation levels using the internal calibration output required in § 11.32(a)(4), shall modulate the transmitter at the maximum possible level, but in no case less than 50% of full channel modulation limits. Measured at peak modulation levels, each of the Attention Signal tones shall be calibrated separately to modulate the transmitter at no less than 40%. These two calibrated modulation levels shall have values that are within 1 dB of each other.

(g) Analog cable systems and digital cable systems with fewer than 5,000 subscribers per headend and wireline video systems and wireless cable systems with fewer than 5,000 subscribers shall transmit EAS audio messages in the same order specified in paragraph (a) of this section on at least one channel. The Attention signal may be produced from a storage device. Additionally, these analog cable systems, digital cable systems, and wireless cable systems:

(1) Must install, operate, and maintain equipment capable of generating the EAS codes. The modulation levels for the EAS codes and Attention Signal for analog cable systems shall comply with the aural signal requirements in § 76.605 of this chapter,

(2) Must provide a video interruption and an audio alert message on all channels. The audio alert message must state which channel is carrying the EAS video and audio message,

(3) Shall transmit a visual EAS message on at least one channel. The visual message shall comply with the requirements in paragraph (d) of this section.

(4) May elect not to interrupt EAS messages from broadcast stations based upon a written agreement between all concerned. Further, analog cable systems, digital cable systems, and wireless cable systems may elect not to interrupt the programming of a broadcast station carrying news or weather related emergency information with state and local EAS messages based on a written agreement between all parties.

(5) Wireless cable systems and digital cable systems with a requirement to carry the audio and video EAS message on at least one channel and a requirement to provide video interrupt and an audio alert message on all other channels stating which channel is carrying the audio and video EAS message, may comply by using a means on all programmed channels that automatically tunes the subscriber's set-top box to a pre-designated channel which carries the required audio and video EAS messages.

(h) Analog cable systems and digital cable systems with 10,000 or more subscribers; analog cable and digital cable systems serving 5,000 or more, but less than 10,000 subscribers per headend; and wireline video systems and wireless cable systems with 5,000 or more subscribers shall transmit EAS audio messages in the same order specified in paragraph (a) of this section. The Attention signal may be produced from a storage device. Additionally, these analog cable systems, digital cable systems, and wireless cable systems:

(1) Must install, operate, and maintain equipment capable of generating the EAS codes. The modulation levels for the EAS codes and Attention Signal for analog cable systems shall comply with the aural signal requirements in § 76.605 of this chapter. This will provide sufficient signal levels to operate subscriber television and radio receivers equipped with EAS decoders and to audibly alert subscribers. Wireless cable systems and digital cable systems shall also provide sufficient signal levels to operate subscriber television and radio receivers equipped with EAS decoders and to audibly alert subscribers.

(2) Shall transmit the EAS audio message required in paragraph (a) of this section on all downstream channels.

(3) Shall transmit the EAS visual message on all downstream channels. The visual message shall comply with the requirements in paragraph (d) of this section.

(4) May elect not to interrupt EAS messages from broadcast stations based upon a written agreement between all concerned. Further, analog cable systems, digital cable systems, and wireless cable systems may elect not to interrupt the programming of a broadcast station carrying news or weather related emergency information with state and local EAS messages based on a written agreement between all parties.

(5) Wireless cable systems and digital cable systems with a requirement to carry the audio and video EAS message on all downstream channels may comply by using a means on all programmed channels that automatically tunes the subscriber's set-top box to a pre-designated channel which carries the required audio and video EAS messages.

(i) SDARS licensees shall transmit national audio EAS messages on all channels in the same order specified in paragraph (a) of this section.

(1) SDARS licensees must install, operate, and maintain equipment capable of generating the EAS codes.

(2) SDARS licensees may determine the distribution methods they will use to comply with this requirement.

(j) DBS providers shall transmit national audio and visual EAS messages on all channels in the same order specified in paragraph (a) of this section.

(1) DBS providers must install, operate, and maintain equipment capable of generating the EAS codes.

(2) The visual message shall comply with the requirements in paragraph (d) of this section.

(3) DBS providers may determine the distribution methods they will use to comply with this requirement. Such methods may include distributing the EAS message on all channels, using a means to automatically tune the subscriber's set-top box to a pre-designated channel which carries the required audio and video EAS messages, and/or passing through the EAS message provided by programmers and/or local channels (where applicable).

(k) If manual interrupt is used as authorized in paragraph (m) of this section, EAS Encoders must be located so that EAS Participant staff, at normal duty locations, can initiate the EAS code and Attention Signal transmission.

(l) EAS Participants that are co-owned and co-located with a combined studio or control facility, (such as an AM and FM licensed to the same entity and at the same location or a cable headend serving more than one system) may provide the EAS transmitting requirements contained in this section for the combined stations or systems with one EAS Encoder. The requirements of § 11.32 must be met by the combined facility.

(m) EAS Participants are required to transmit all received EAS messages in which the header code contains the Event code for National Emergency Message (EAN), Nationwide Test of the Emergency Alert System (NPT), or Required Monthly Test (RMT), and when the accompanying location codes include their State or State/county. These EAS messages shall be retransmitted unchanged except for the LLLLLLLL-code which identifies the EAS Participant retransmitting the message. See § 11.31(c). If an EAS source originates an EAS message with any of the Event codes listed in this paragraph, it must include the location codes for the State(s) and counties in its service area. When transmitting the required weekly test, EAS Participants shall use the event code RWT. The location codes are the state and county for the broadcast station city of license or system community or city. Other location codes may be included upon approval of station or system management. EAS messages may be transmitted automatically or manually.

(1) Automatic interrupt of programming and transmission of EAS messages are required when facilities are unattended. Automatic transmissions must include a permanent record that contains at a minimum the following information: Originator, Event, Location and valid time period of the message. The decoder performs the functions necessary to determine which EAS messages are automatically transmitted by the encoder.

(2) Manual interrupt of programming and transmission of EAS messages may be used. EAS messages with the National Emergency Message (EAN) Event code or the Nationwide Test of the Emergency Alert System (NPT) Event code must be transmitted immediately. Monthly EAS test messages must be transmitted within 60 minutes. All actions must be logged and include the minimum information required for EAS video messages.

(n) EAS Participants may employ a minimum delay feature, not to exceed 15 minutes, for automatic interruption of EAS codes. However, this may not be used for the EAN Event code, or the NPT Event code in the case of a nationwide test of the EAS, which must be transmitted immediately. The delay time for an RMT message may not exceed 60 minutes.

(o) Either manual or automatic operation of EAS equipment may be used by EAS Participants that use remote control. If manual operation is used, an EAS decoder must be located at the remote control location and it must directly monitor the signals of the two assigned EAS sources. If direct monitoring of the assigned EAS sources is not possible at the remote location, automatic operation is required. If automatic operation is used, the remote control location may be used to override the transmission of an EAS alert. EAS Participants may change back and forth between automatic and manual operation.

(p) The material listed in this paragraph (p) is incorporated by reference into this section with the approval of the Director of the Federal Register under 5 U.S.C. 552(a) and 1 CFR part 51. To enforce any edition other than that specified in this section, the Federal Communications Commission (FCC) must publish notice of change in the *Federal Register* and the material must be available to the public. All approved material is available for inspection at the FCC and at the National Archives and Records Administration (NARA). Contact FCC at: the address indicated in 47 CFR 0.401(a) of this chapter (Reference Information Center). For information on the availability of this material at NARA, email: *fr.inspection@nara.gov,* or go to: *www.archives.gov/federal-register/cfr/ibr-locations.html.* The material may be obtained from the following source in this paragraph (p).

[70 FR 71035, Nov. 25, 2005, as amended at 71 FR 76220, Dec. 20, 2006; 72 FR 62135, Nov. 2, 2007; 71 FR 76220, Dec. 20, 2006; 72 FR 62135, Nov. 2, 2007; 77 FR 16704, Mar. 22, 2012; 80 FR 37175, June 30, 2015; 85 FR 64406, Oct. 13, 2020; 87 FR 67824, Nov. 10, 2022; 91 FR 2872, Jan. 23, 2026]

### § 11.52 EAS code and Attention Signal Monitoring requirements.

(a) EAS Participants must be capable of receiving the Attention Signal required by § 11.31(a)(2) and emergency messages of other broadcast stations during their hours of operation. EAS Participants must install and operate during their hours of operation, equipment that is capable of receiving and decoding, either automatically or manually, the EAS header codes, emergency messages and EOM code, and which complies with the requirements in § 11.56.

**Note to paragraph (**a**):**

The two-tone Attention Signal will not be used to actuate two-tone decoders but will be used as an aural alert signal.

(b) If manual interrupt is used as authorized in § 11.51(m)(2), decoders must be located so that operators at their normal duty stations can be alerted immediately when EAS messages are received.

(c) EAS Participants that are co-owned and co-located with a combined studio or control facility (such as an AM and FM licensed to the same entity and at the same location or a cable headend serving more than one system) may comply with the EAS monitoring requirements contained in this section for the combined station or system with one EAS Decoder. The requirements of § 11.33 must be met by the combined facilities. Co-located LPFM stations including those operating on a time-sharing basis but which, pursuant to ownership restrictions in § 73.855 of this chapter cannot be co-owned, may also comply with the EAS monitoring requirements with one EAS Decoder pursuant to a written agreement between the licensees ensuring that each licensee has access to the decoder; that the stations will jointly meet the requirements of § 11.33; and that each licensee remains fully and individually responsible for compliance with all EAS rules and obligations applicable to LPFM EAS participants in this part, and any EAS violations involving the shared, co-located equipment. Each LPFM licensee entering into such an arrangement remains fully and directly liable for enforcement actions involving the shared equipment as well as all other obligations attendant to LPFM EAS Participants in this part, regardless of which party to the agreement took or failed to take the actions giving rise to the violation.

(d) EAS Participants must comply with the following monitoring requirements:

(1) With respect to monitoring for EAS messages that are formatted in accordance with the EAS Protocol, EAS Participants must monitor two EAS sources. The monitoring assignments of each broadcast station and cable system and wireless cable system are specified in the State EAS Plan and FCC Mapbook. They are developed in accordance with FCC monitoring priorities.

(2) With respect to monitoring EAS messages formatted in accordance with the specifications set forth in § 11.56(a)(2), EAS Participants' EAS equipment must regularly poll the Federal Emergency Management Agency's Integrated Public Alert and Warning System (IPAWS) EAS alert distribution channel to detect and acquire Common Alert Protocol (CAP)-formatted alert messages from the IPAWS system to EAS Participants' EAS equipment.

(3) If the required EAS message sources cannot be received, alternate arrangements or a waiver may be obtained by written request to the Chief, Public Safety and Homeland Security Bureau. In an emergency, a waiver may be issued over the telephone with a follow up letter to confirm temporary or permanent reassignment.

(4) The management of EAS Participants shall determine which header codes will automatically interrupt their programming for State and Local Area emergency situations affecting their audiences.

(e) EAS Participants are required to interrupt normal programming either automatically or manually when they receive an EAS message in which the header code contains the Event codes for National Emergency Message (EAN), the Nationwide Test of the Emergency Alert System (NPT), or the Required Monthly Test (RMT) for their State or State/county location.

[70 FR 71036, Nov. 25, 2005, as amended at 77 FR 16705, Mar. 22, 2012; 80 FR 37176, June 30, 2015; 83 FR 37759, Aug. 2, 2018; 85 FR 35572, June 11, 2020; 87 FR 67825, Nov. 10, 2022]

### § 11.53 [Reserved]

### § 11.54 EAS operation during a National Level emergency.

(a) Immediately upon receipt of an EAN message, or the NPT Event code in the case of a nationwide test of the EAS, EAS Participants must comply with the following requirements, as applicable:

(1) Analog and digital broadcast stations may transmit their call letters and analog cable systems, digital cable systems and wireless cable systems may transmit the names of the communities they serve during an EAS activation. State and Local Area identifications must be given as provided in State and Local Area EAS Plans.

(2) Analog and digital broadcast stations are exempt from complying with §§ 73.62 and 73.1560 of this chapter (operating power maintenance) while operating under this part.

(3) The time of receipt of the EAN shall be entered by analog and digital broadcast stations in their logs (as specified in §§ 73.1820 and 73.1840 of this chapter), by analog and digital cable systems in their records (as specified in § 76.1711 of this chapter), by subject wireless cable systems in their records (as specified in § 21.304 of this chapter), and by all other EAS Participants in their records as specified in § 11.35(a).

(b) EAS Participants originating emergency communications under this section shall be considered to have conferred rebroadcast authority, as required by section 325(a) of the Communications Act of 1934, 47 U.S.C. 325(a), to other EAS Participants.

(c) During a national level EAS emergency, EAS Participants may transmit in lieu of the EAS audio feed an audio feed of the President's voice message from an alternative source, such as a broadcast network audio feed.

[77 FR 16705, Mar. 22, 2012, as amended at 80 FR 37177, June 30, 2015]

### § 11.55 EAS operation during a State or Local Area emergency.

(a) The EAS may be activated at the State and Local Area levels by EAS Participants at their discretion for day-to-day emergency situations posing a threat to life and property. Examples of natural emergencies which may warrant state EAS activation are: Tornadoes, floods, hurricanes, earthquakes, heavy snows, icing conditions, widespread fires, etc. Man-made emergencies warranting state EAS activation may include: Toxic gas leaks or liquid spills, widespread power failures, industrial explosions, and civil disorders.

(1) DBS providers shall pass through all EAS messages aired on local television broadcast stations carried by DBS providers under the Commission's broadcast signal carriage rules to subscribers receiving those channels.

(2) SDARS licensees and DBS providers may participate in EAS at the state and local level and make their systems capable of receiving and transmitting state and local level EAS messages on all channels. If an SDARS licensee or DBS provider is not capable of receiving and transmitting state and local EAS message on all channels, it must inform its subscribers, on its website and in writing on an annual basis, of which channels are and are not capable of supplying state and local messages.

(b) EAS operations must be conducted as specified in State and Local Area EAS Plans.

(c) An EAS Participant that participates in the State or Local Area EAS, upon receipt of a State or Local Area EAS message that has been formatted in the EAS Protocol and that has event and location header codes indicating that it is a type of message that the EAS Participant normally relays, consistent with the procedures in the State or Local Area EAS Plan, must do the following:

(1) Prior to December 12, 2023, the EAS Participant shall follow the procedures set forth in the State EAS Plan and paragraphs (c)(3) through(7) of this section.

(2) On and after December 12, 2023,—

(i) *CAP Prioritization.* If a message formatted in the Common Alerting Protocol is available that is a duplicate of the received message formatted in the EAS Protocol, then the EAS Participant shall not transmit the received message formatted in the EAS Protocol but shall follow the procedures in paragraph (d) of this section to transmit the message formatted in the Common Alerting Protocol.

(ii) *Polling.* At least ten (10) seconds after detecting the initial header code of a received message formatted in the EAS protocol, if the EAS Participant has not by that time determined that a duplicate message formatted in the Common Alerting Protocol is available, it shall poll the Federal Emergency Management Agency's Integrated Public Alert and Warning System (IPAWS) at least once to determine whether a duplicate CAP-formatted alert message is available.

(A) If a duplicate CAP-formatted alert message is available, the EAS Participant shall proceed according to paragraphs (c)(2)(i) and (d) of this section.

(B) If no duplicate CAP-formatted alert message is available, or if the alert contents, including the audio message, cannot be acquired within a reasonable timeframe, the EAS Participant shall proceed according to paragraphs (c)(3)-(7) of this section.

(iii) For purposes of this paragraph (c)(2), two EAS messages are “duplicates” if the originator codes, event codes, location codes, and date-time codes in the validated headers of both messages are all identical, and the valid time-period codes in the headers of both messages cover approximately the same periods of time, with allowances for the different manners in which messages in CAP and legacy EAS formats express valid time periods.

(3) EAS Participants participating in the State or Local Area EAS must discontinue normal programming and follow the procedures in their State and Local Area Plans. Analog and digital television broadcast stations must transmit all EAS announcements visually and aurally as specified in § 11.51(a) through (e) and 73.1250(h) of this chapter, as applicable; analog cable systems, digital cable systems, wireless cable systems, and wireline video systems must transmit all EAS announcements visually and aurally as specified in § 11.51(d), (g), and (h); and DBS providers must transmit all EAS announcements visually and aurally as specified in § 11.51(d) and (j). EAS Participants providing foreign language programming should transmit all EAS announcements in the same language as the primary language of the EAS Participant.

(4) Upon completion of the State or Local Area EAS transmission procedures, resume normal programming until receipt of the cue from the SR or LP sources in your Local Area. At that time begin transmitting the common emergency message received from the above sources.

(5) Resume normal operations upon conclusion of the message.

(6) The times of the above EAS actions must be entered in the EAS Participants' records as specified in §§ 11.35(a) and 11.54(a)(3).

(7) Use of the EAS codes or Attention Signal automatically grants rebroadcast authority as specified in § 11.54(b).

(d) An EAS Participant that participates in the State or Local Area EAS, upon receipt of a State or Local Area EAS message that has been formatted in the Common Alerting Protocol and that has event and location header codes indicating that it is a type of message that the EAS Participant normally relays, must do the following:

(1) EAS Participants participating in the State or Local Area EAS must follow the procedures for processing such messages in the State and Local Area Plans.

(2) Analog and digital television broadcast stations must transmit all EAS announcements visually and aurally as specified in § 11.51(a) through (e) and 73.1250(h) of this chapter, as applicable; analog cable systems, digital cable systems, wireless cable systems, and wireline video systems must transmit all EAS announcements visually and aurally as specified in § 11.51(d), (g), and (h); and DBS providers must transmit all EAS announcements visually and aurally as specified in § 11.51(d) and (j). EAS Participants providing foreign language programming should transmit all EAS announcements in the same language as the primary language of the EAS Participant.

(3) Resume normal operations upon conclusion of the message.

(4) The times of the above EAS actions must be entered in the EAS Participants' records as specified in §§ 11.35(a) and 11.54(a)(3).

[59 FR 67092, Dec. 28, 1994, as amended at 63 FR 29666, June 1, 1998; 65 FR 21658, Apr. 24, 2000; 67 FR 18511, Apr. 16, 2002; 70 FR 71037, Nov. 25, 2005; 71 FR 76220, Dec. 20, 2006; 72 FR 62135, Nov. 2, 2007; 77 FR 16706, Mar. 22, 2012; 83 FR 37759, Aug. 2, 2018; 87 FR 67825, Nov. 10, 2022]

### § 11.56 Obligation to process CAP-formatted EAS messages.

(a) On or by June 30, 2012, EAS Participants must have deployed operational equipment that is capable of the following:

(1) Acquiring EAS alert messages in accordance with the monitoring requirements in § 11.52(d)(2);

(2) Converting EAS alert messages that have been formatted pursuant to the Organization for the Advancement of Structured Information Standards (OASIS) Common Alerting Protocol Version 1.2 (July 1, 2010), and Common Alerting Protocol, v. 1.2 USA Integrated Public Alert and Warning System Profile Version 1.0 (Oct. 13, 2009), into EAS alert messages that comply with the EAS Protocol, such that the Preamble and EAS Header Codes, audio Attention Signal, audio message, and Preamble and EAS End of Message (EOM) Codes of such messages are rendered equivalent to the EAS Protocol (set forth in § 11.31), in accordance with the technical specifications governing such conversion process set forth in the EAS-CAP Industry Group's (ECIG) Recommendations for a CAP EAS Implementation Guide, Version 1.0 (May 17, 2010) (except that any and all specifications set forth therein related to gubernatorial “must carry” shall not be followed, and that EAS Participants may adhere to the specifications related to text-to-speech on a voluntary basis).

(3) Processing such converted messages in accordance with the other sections of this part.

(b) EAS Participants may comply with the requirements of this section by deploying an Intermediary Device. If an EAS Participant elects to meet the requirements of this section by deploying an Intermediary Device, it shall be required to construct visual messages from CAP-formatted EAS messages in accordance with § 3.6 of the “ECIG Recommendations for a CAP EAS Implementation Guide, Version 1.0” (May 17, 2010), as set forth in §§ 11.51(d), (g)(3), (h)(3), and (j)(2) of this part, on or by June 30, 2015.

(c) EAS Participants shall configure their systems to reject all CAP-formatted EAS messages that include an invalid digital signature.

(d) The material listed in this paragraph (d) is incorporated by reference into this section with the approval of the Director of the Federal Register under 5 U.S.C. 552(a) and 1 CFR part 51. To enforce any edition other than that specified in this section, the Federal Communications Commission (FCC) must publish notice of change in the *Federal Register* and the material must be available to the public. All approved material is available for inspection at the FCC and at the National Archives and Records Administration (NARA). Contact FCC at: the address indicated in 47 CFR 0.401(a) of this chapter (Reference Information Center). For information on the availability of this material at NARA, email: *fr.inspection@nara.gov,* or go to: *http://www.archives.gov/federal-register/cfr/ibr-locations.html.* The material may be obtained from the following sources in this paragraph (d).

(1) The following standard is available from the EAS-CAP Industry Group (ECIG), 21010 Southbank Street, #365, Sterling, VA 20165, or go to *http://www.eas-cap.org.*

(i) “ECIG Recommendations for a CAP EAS Implementation Guide, Version 1.0” (May 17, 2010).

(ii) [Reserved]

(2) The following standards are available from Organization for the Advancement of Structured Information Standards (OASIS), 25 Corporate Drive, Suite 103, Burlington, MA 01803-4238, call 781-425-5073, or go to *http://www.oasis-open.org.*

(i) “Common Alerting Protocol Version 1.2” (July 1, 2010).

(ii) “Common Alerting Protocol, v. 1.2 USA Integrated Public Alert and Warning System Profile Version 1.0” (Oct. 13, 2009).

[77 FR 16706, Mar. 22, 2012, as amended at 77 FR 26703, May 7, 2012; 83 FR 39621, Aug. 10, 2018; 85 FR 64406, Oct. 13, 2020; 87 FR 67826, Nov. 10, 2022]

## Subpart E—Tests

### § 11.61 Tests of EAS procedures.

(a) EAS Participants shall conduct tests at regular intervals, as specified in paragraphs (a)(1) and (a)(2) of this section. Additional tests may be performed anytime. EAS activations and special tests may be performed in lieu of required tests as specified in paragraph (a)(4) of this section.

(1) Required Monthly Tests of the EAS header codes, Attention Signal, Test Script and EOM code.

(i) Tests in odd numbered months shall occur between 8:30 a.m. and local sunset. Tests in even numbered months shall occur between local sunset and 8:30 a.m. They will originate from Local or State Primary sources. The time and script content will be developed by State Emergency Communications Committees in cooperation with affected EAS Participants. Script content may be in the primary language of the EAS Participant. These monthly tests must be transmitted within 60 minutes of receipt by EAS Participants in an EAS Local Area or State. Analog and digital class D non-commercial educational FM, analog and digital LPFM stations, and LPTV stations are required to transmit only the test script.

(ii) Effective May 31, 2007, DBS providers must comply with this section by monitoring a state or local primary source to participate in testing. Tests should be performed on 10% of all channels monthly (excluding local-into-local channels for which the monthly transmission tests are passed through by the DBS provider), with channels tested varying from month to month, so that over the course of a given year, 100% of all channels are tested.

(iii) SDARS providers must comply with this section by monitoring a state or local primary source to participate in testing. Tests should be performed on 10% of all channels monthly, with channels tested varying from month to month, so that over the course of a given year, 100% of all channels are tested.

(iv) Upon receipt of an EAS message in the EAS Protocol format with the Required Monthly Test (RMT) event code, an EAS Participant shall follow the steps set forth in § 11.55(c)(1) through(3).

(2) Required Weekly Tests:

(i) EAS Header Codes and EOM Codes:

(A) Analog and digital AM, FM, and TV broadcast stations must conduct tests of the EAS header and EOM codes at least once a week at random days and times. DAB and TV stations must conduct these tests on all program streams.

(B) Analog cable systems and digital cable systems with 5,000 or more subscribers per headend and wireless cable systems with 5,000 or more subscribers must conduct tests of the EAS Header and EOM Codes at least once a week at random days and times on all programmed channels.

(C) Analog cable systems and digital cable systems serving fewer than 5,000 subscribers per headend and wireless cable systems with fewer than 5,000 subscribers must conduct tests of the EAS Header and EOM Codes at least once a week at random days and times on at least one programmed channel.

(ii) DBS providers, SDARS providers, analog and digital class D non-commercial educational FM stations, analog and digital LPFM stations, and LPTV stations are not required to transmit this test but must log receipt, as specified in § 11.35(a) and 11.54(a)(3).

(iii) The EAS weekly test is not required during the week that a monthly test is conducted.

(iv) EAS Participants are not required to transmit a video message when transmitting the required weekly test.

(3) *Nationwide Tests of the Emergency Alert System (NPT) (national tests).* (i) All EAS Participants shall participate in national tests as scheduled by the Commission in consultation with the Federal Emergency Management Agency (FEMA). Such tests will consist of the delivery by FEMA to PEP/NP stations of a coded EAS message, including EAS header codes, Attention Signal, Test Script, and EOM code. All other EAS Participants will then be required to relay that EAS message. The coded message shall utilize EAS test codes as designated by the Commission's rules.

(ii) A national test shall replace the required weekly and monthly tests for all EAS Participants, as set forth in paragraphs (a)(1) and (a)(2) of this section, in the week and month in which it occurs.

(iii) Notice shall be provided to EAS Participants by the Commission at least two months prior to the conduct of any such national test.

(iv) Test results as required by the Commission shall be logged by all EAS Participants into the EAS Test Reporting System (ETRS) as determined by the Commission's Public Safety and Homeland Security Bureau, subject to the following requirements.

(A) EAS Participants shall provide the identifying information required by the ETRS initially no later than sixty days after the publication in the *Federal Register* of a notice announcing the approval by the Office of Management and Budget of the modified information collection requirements under the Paperwork Reduction Act of 1995 and an effective date of the rule amendment, or within sixty days of the launch of the ETRS, whichever is later, and shall renew this identifying information on a yearly basis or as required by any revision of the EAS Participant's State EAS Plan filed pursuant to § 11.21.

(B) “Day of test” data shall be filed in the ETRS within 24 hours of any nationwide test or as otherwise required by the Public Safety and Homeland Security Bureau.

(C) Detailed post-test data shall be filed in the ETRS within forty five (45) days following any nationwide test.

(4) *EAS activations and special tests.* The EAS may be activated for emergencies or special tests at the State or Local Area level by an EAS Participant instead of the monthly or weekly tests required by this section. To substitute for a monthly test, activation must include transmission of the EAS header codes, Attention Signal, emergency message and EOM code and comply with the visual message requirements in § 11.51. To substitute for the weekly test of the EAS header codes and EOM codes in paragraph (a)(2)(i) of this section, activation must include transmission of the EAS header and EOM codes. Analog and digital television broadcast stations, analog cable systems, digital cable systems, wireless cable systems, and DBS providers shall comply with the aural and visual message requirements in § 11.51. Special EAS tests at the State and Local Area levels may be conducted on daily basis following procedures in State and Local Area EAS plans.

(5) *Live Code Tests.* EAS Participants may participate in no more than two (2) “Live Code” EAS Tests per calendar year that are conducted to exercise the EAS and raise public awareness for it, provided that the entity conducting the test:

(i) Notifies the public before the test that live event codes will be used, but that no emergency is, in fact, occurring;

(ii) To the extent technically feasible, states in the test message that the event is only a test;

(iii) Coordinates the test among EAS Participants and with state and local emergency authorities, the relevant SECC (or SECCs, if the test could affect multiple states), and first responder organizations, such as PSAPs, police, and fire agencies); and,

(iv) Consistent with § 11.51, provides in widely accessible formats the notification to the public required by this subsection that the test is only a test, and is not a warning about an actual emergency.

(b) Entries shall be made in EAS Participant records, as specified in § 11.35(a) and 11.54(a)(3).

[70 FR 71038, Nov. 25, 2005, as amended at 76 FR 12604, Mar. 8, 2011; 77 FR 16707, Mar. 22, 2012; 80 FR 37177, June 30, 2015; 83 FR 39621, Aug. 10, 2018; 85 FR 30634, May 20, 2020; 87 FR 67826, Nov. 10, 2022; 91 FR 2872, Jan. 23, 2026]
