---
title: "45 CFR Part 180 — HOSPITAL PRICE TRANSPARENCY"
identifier: "45 CFR Part 180"
type: regulation
jurisdiction: us
language: en
last_amended: 2026-10-06  # latest amendment date of the CFR title
status: in_force
source: "https://www.ecfr.gov/current/title-45/part-180"
retrieved: 2026-10-11
ecfr_bulk_modified: "07-Oct-2026 21:18"
---

*Title 45—Public Welfare › SUBTITLE A—Department of Health and Human Services › SUBCHAPTER E—PRICE TRANSPARENCY*

# PART 180—HOSPITAL PRICE TRANSPARENCY

**Authority:** 42 U.S.C. 300gg-18, 42 U.S.C. 1302.

**Source:** 84 FR 65602, Nov. 27, 2019, unless otherwise noted.

## Subpart A—General Provisions

### § 180.10 Basis and scope.

This part implements section 2718(e) of the Public Health Service (PHS) Act, which requires each hospital operating within the United States, for each year, to establish, update, and make public a list of the hospital's standard charges for items and services provided by the hospital, including for diagnosis-related groups (DRGs) established under section 1886(d)(4) of the Social Security Act. This part also implements section 2718(b)(3) of the PHS Act, to the extent that section authorizes CMS to promulgate regulations for enforcing section 2718(e). This part also implements section 1102(a) of the Social Security Act, which authorizes the Secretary to make and publish rules and regulations, not inconsistent with that Act, as may be necessary to the efficient administration of the functions for which the Secretary is charged under that Act.

### § 180.20 Definitions.

The following definitions apply to this part, unless specified otherwise:

*Ancillary service* means an item or service a hospital customarily provides as part of or in conjunction with a shoppable primary service.

*Chargemaster (Charge Description Master or CDM)* means the list of all individual items and services maintained by a hospital for which the hospital has established a charge.

*CMS template* means a CSV format or JSON schema that CMS makes available for purposes of compliance with § 180.40(a).

*De-identified maximum negotiated charge* means the highest charge that a hospital has negotiated with all third party payers for an item or service.

*De-identified minimum negotiated charge* means the lowest charge that a hospital has negotiated with all third party payers for an item or service.

*Discounted cash price* means the charge that applies to an individual who pays cash (or cash equivalent) for a hospital item or service.

*Encode* means to convert hospital standard charge information into a machine-readable format that complies with § 180.50(c)(2).

*Estimated allowed amount* means the average dollar amount that the hospital has historically received from a third party payer for an item or service.

*Gross charge* means the charge for an individual item or service that is reflected on a hospital's chargemaster, absent any discounts.

*Hospital* means an institution in any State in which State or applicable local law provides for the licensing of hospitals, that is licensed as a hospital pursuant to such law or is approved, by the agency of such State or locality responsible for licensing hospitals, as meeting the standards established for such licensing. For purposes of this definition, a State includes each of the several States, the District of Columbia, Puerto Rico, the Virgin Islands, Guam, American Samoa, and the Northern Mariana Islands.

*Items and services* means all items and services, including individual items and services and service packages, that could be provided by a hospital to a patient in connection with an inpatient admission or an outpatient department visit for which the hospital has established a standard charge. Examples include, but are not limited to, the following:

(1) Supplies and procedures.

(2) Room and board.

(3) Use of the facility and other items (generally described as facility fees).

(4) Services of employed physicians and non-physician practitioners (generally reflected as professional charges).

(5) Any other items or services for which a hospital has established a standard charge.

*Machine-readable file* means a single digital file that is in a machine-readable format.

*Machine-readable format* means a digital representation of data or information in a file that can be imported or read into a computer system for further processing.

*Payer-specific negotiated charge* means the charge that a hospital has negotiated with a third party payer for an item or service.

*Median allowed amount* means the median of the total allowed amounts the hospital has historically received from a third party payer for an item or service for a time period no less than 12 months and no longer than 15 months prior to posting the machine-readable file. Should the calculated median fall between two observed allowed amounts, the median allowed amount is the next highest observed value.

*Ninetieth (90th) percentile allowed amount* means the 90th percentile of the total allowed amounts the hospital has historically received from a third party payer for an item or service for a time period no less than 12 months and no longer than 15 months prior to posting the machine-readable file. Should the calculated percentile fall between two observed allowed amounts, the 90th percentile allowed amount is the next highest observed value.

*Service package* means an aggregation of individual items and services into a single service with a single charge.

*Shoppable service* means a service that can be scheduled by a healthcare consumer in advance.

*Standard charge* means the regular rate established by the hospital for an item or service provided to a specific group of paying patients. This includes all of the following as defined under this section:

(1) Gross charge.

(2) Payer-specific negotiated charge.

(3) De-identified minimum negotiated charge.

(4) De-identified maximum negotiated charge.

(5) Discounted cash price.

*State forensic hospital* means a public psychiatric hospital that provides treatment for individuals who are in the custody of penal authorities.

*Tenth (10th) percentile allowed amount* means the 10th percentile of the total allowed amounts the hospital has historically received from a third party payer for an item or service for a time period no less than 12 months and no longer than 15 months prior to posting the machine-readable file. Should the calculated percentile fall between two observed allowed amounts, the 10th percentile allowed amount is the next highest observed value.

*Third party payer* means an entity that is, by statute, contract, or agreement, legally responsible for payment of a claim for a healthcare item or service.

[84 FR 65602, Nov. 27, 2019, as amended at 86 FR 63998, Nov. 16, 2021; 88 FR 82184, Nov. 22, 2023; 90 FR 54087, Nov. 25, 2025]

### § 180.30 Applicability.

(a) *General applicability.* Except as provided in paragraph (b) of this section, the requirements of this part apply to hospitals as defined at § 180.20.

(b) *Exception.* Federal and State hospitals are deemed by CMS to be in compliance with the requirements of this part including but not limited to:

(1) Federally owned hospital facilities, including facilities operated by the U.S. Department of Veterans Affairs and Military Treatment Facilities operated by the U.S. Department of Defense.

(2) Hospitals operated by an Indian Health Program as defined in section 4(12) of the Indian Health Care Improvement Act.

(3) State forensic hospitals that provide treatment exclusively to individuals who are in the custody of penal authorities.

(c) *Online availability.* Unless otherwise stated, hospital charge information must be made public electronically via the internet.

[84 FR 65602, Nov. 27, 2019, as amended at 86 FR 63998, Nov. 16, 2021]

## Subpart B—Public Disclosure Requirements

### § 180.40 General requirements.

A hospital must make public the following:

(a) A machine-readable file containing a list of all standard charges for all items and services as provided in § 180.50.

(b) A consumer-friendly list of standard charges for a limited set of shoppable services as provided in § 180.60.

### § 180.50 Requirements for making public hospital standard charges for all items and services.

(a) *General rules.* (1) A hospital must establish, update, and make public a list of all standard charges for all items and services online in the form and manner specified in this section.

(2) Each hospital location operating under a single hospital license (or approval) that has a different set of standard charges than the other location(s) operating under the same hospital license (or approval) must separately make public the standard charges applicable to that location.

(3) Each hospital must:

(i) Beginning January 1, 2024 through December 31, 2025, make a good faith effort to ensure that the standard charge information encoded in the machine-readable file is true, accurate, and complete as of the date indicated in the machine-readable file.

(ii) Beginning January 1, 2024 through December 31, 2025, affirm in its machine-readable file that, to the best of its knowledge and belief, the hospital has included all applicable standard charge information in accordance with the requirements of this section, and that the information encoded is true, accurate, and complete as of the date indicated in the machine-readable file.

(iii) Beginning January 1, 2026, attest in its machine-readable file the following: To the best of its knowledge and belief, this hospital has included all applicable standard charge information in accordance with the requirements of 45 CFR 180.50, and the information encoded is true, accurate, and complete as of the date in the file. This hospital has included all payer-specific negotiated charges in dollars that can be expressed as a dollar amount. For payer-specific negotiated charges that cannot be expressed as a dollar amount in the machine-readable file or not knowable in advance, the hospital attests that the payer-specific negotiated charge is based on a contractual algorithm, percentage or formula that precludes the provision of a dollar amount and has provided all necessary information available to the hospital for the public to be able to derive the dollar amount, including, but not limited to, the specific fee schedule or components referenced in such percentage, algorithm or formula.

(iv) Beginning January 1, 2026, encode the name of the hospital chief executive officer, president, or senior official designated to oversee the encoding of true, accurate, and complete data as directed in in paragraph (a)(3)(iii) of this section.

(b) *Required data elements.* (1) Prior to July 1, 2024, a hospital must include all of the following corresponding data elements in its list of standard charges, as applicable:

(i) Description of each item or service provided by the hospital.

(ii) Gross charge that applies to each individual item or service when provided in, as applicable, the hospital inpatient setting and outpatient department setting.

(iii) Payer-specific negotiated charge that applies to each item or service when provided in, as applicable, the hospital inpatient setting and outpatient department setting. Each payer-specific negotiated charge must be clearly associated with the name of the third party payer and plan.

(iv) De-identified minimum negotiated charge that applies to each item or service when provided in, as applicable, the hospital inpatient setting and outpatient department setting.

(v) De-identified maximum negotiated charge that applies to each item or service when provided in, as applicable, the hospital inpatient setting and outpatient department setting.

(vi) Discounted cash price that applies to each item or service when provided in, as applicable, the hospital inpatient setting and outpatient department setting.

(vii) Any code used by the hospital for purposes of accounting or billing for the item or service, including, but not limited to, the Current Procedural Terminology (CPT) code, the Healthcare Common Procedure Coding System (HCPCS) code, the Diagnosis Related Group (DRG), the National Drug Code (NDC), or other common payer identifier.

(2) Unless otherwise specified in this paragraph (b)(2), beginning July 1, 2024, each hospital must encode in its machine-readable file all standard charge information, as applicable, for each of the following required data elements:

(i) General data elements, including:

(A) Hospital name, license number, location name(s) and address(es) under the single hospital license to which the list of standard charges applies, and beginning January 1, 2026, Type 2 (organizational) National Provider Identifier(s) (NPI). Location name(s) and address(es) must include, at minimum, all inpatient facilities and stand-alone emergency departments; and

(B) The version number of the CMS template and the date of most recent update to the standard charge information in the machine-readable file.

(ii) Each type of standard charge as defined at § 180.20 (gross charge, discounted cash price, payer-specific negotiated charge, de-identified minimum negotiated charge, and de-identified maximum negotiated charge) and, for payer-specific negotiated charges, the following additional data elements:

(A) Payer and plan names; plan(s) may be indicated as categories (such as “all PPO plans”) when the established payer-specific negotiated charges are applicable to each plan in the indicated category;

(B) Method used to establish the standard charge; and

(C) Whether the standard charge indicated should be interpreted by the user as a dollar amount, or if the standard charge is based on a percentage or algorithm. If the standard charge is based on a percentage or algorithm, the machine-readable file (MRF) must also describe the percentage or algorithm that determines the dollar amount for the item or service, and

(*1*) Beginning January 1, 2025 through December 31, 2025, calculate and encode an estimated allowed amount in dollars for that item or service; and

(*2*) Beginning January 1, 2026, calculate and encode the tenth (10th) percentile allowed amount, the median allowed amount, and the ninetieth (90th) percentile allowed amount in dollars for that item or service. Hospitals must also calculate and encode the total number of allowed amount remittances that were used to calculate the 10th percentile allowed amount, median allowed amount, and 90th percentile allowed amount.

(iii) A description of the item or service that corresponds to the standard charge established by the hospital, including:

(A) A general description of the item or service;

(B) Whether the item or service is provided in connection with an inpatient admission or an outpatient department visit; and

(C) Beginning January 1, 2025, for drugs, the drug unit and type of measurement.

(iv) Coding information, including:

(A) Any code(s) used by the hospital for purposes of accounting or billing for the item or service;

(B) Corresponding code type(s). Such code types may include, but are not limited to, the CPT code, the HCPCS code, the DRG, the NDC, Revenue Center Codes (RCC), or other common payer identifier; and

(C) Beginning January 1, 2025, any modifier(s) that may change the standard charge that corresponds to a hospital item or service, including a description of the modifier and how it changes the standard charge.

(c) *Format.* (1) Prior to July 1, 2024, the information described in paragraph (b)(1) of this section must be published in a single digital file that is in a machine-readable format.

(2) Beginning July 1, 2024, the hospital's machine-readable file must conform to a CMS template layout, data specifications, and data dictionary for purposes of making public the standard charge information required under paragraph (b)(2) of this section.

(d) *Location and accessibility.* (1) A hospital must select a publicly available website for purposes of making public the standard charge information required under paragraph (b) of this section.

(2) The standard charge information must be displayed in a prominent manner and clearly identified with the hospital location with which the standard charge information is associated.

(3) The hospital must ensure that the standard charge information is easily accessible, without barriers, including but not limited to ensuring the information is accessible:

(i) Free of charge;

(ii) Without having to establish a user account or password;

(iii) Without having to submit personal identifying information (PII); and

(iv) To automated searches and direct file downloads through a link posted on a publicly available website.

(4) The machine-readable file and standard charge information contained in that machine-readable file must be digitally searchable.

(5) The machine-readable file must use the following naming convention specified by CMS, specifically: &lt;ein>\_&lt;hospital-name>\_standardcharges. [json|csv].

(6) Beginning January 1, 2024, the hospital must ensure that the public website it selects to host its machine-readable file establishes and maintains, in the form and manner specified by CMS:

(i) A .txt file in the root folder that includes:

(A) The hospital location name that corresponds to the machine-readable file;

(B) The source page URL that hosts the machine-readable file;

(C) A direct link to the machine-readable file (the machine-readable file URL); and

(D) Hospital point of contact information.

(ii) A link in the footer on its website, including but not limited to the homepage, that is labeled “Price Transparency” and links directly to the publicly available web page that hosts the link to the machine-readable file.

(e) *Frequency of updates.* The hospital must update the standard charge information described in paragraph (b) of this section at least once annually.

[84 FR 65602, Nov. 27, 2019, as amended at 86 FR 63998, Nov. 16, 2021; 88 FR 82184, Nov. 22, 2023; 90 FR 54087, Nov. 25, 2025]

### § 180.60 Requirements for displaying shoppable services in a consumer-friendly manner.

(a) *General rules.* (1) A hospital must make public the standard charges identified in paragraphs (b)(3) through (6) of this section, for as many of the 70 CMS-specified shoppable services that are provided by the hospital, and as many additional hospital-selected shoppable services as is necessary for a combined total of at least 300 shoppable services.

(i) In selecting a shoppable service for purposes of this section, a hospital must consider the rate at which it provides and bills for that shoppable service.

(ii) If a hospital does not provide 300 shoppable services, the hospital must make public the information specified in paragraph (b) of this section for as many shoppable services as it provides.

(2) A hospital is deemed by CMS to meet the requirements of this section if the hospital maintains an internet-based price estimator tool which meets the following requirements.

(i) Provides estimates for as many of the 70 CMS-specified shoppable services that are provided by the hospital, and as many additional hospital-selected shoppable services as is necessary for a combined total of at least 300 shoppable services.

(ii) Allows healthcare consumers to, at the time they use the tool, obtain an estimate of the amount they will be obligated to pay the hospital for the shoppable service.

(iii) Is prominently displayed on the hospital's website and accessible to the public without charge and without having to register or establish a user account or password.

(b) *Required data elements.* A hospital must include, as applicable, all of the following corresponding data elements when displaying its standard charges (identified in paragraphs (b)(3) through (6) of this section) for its list of shoppable services selected under paragraph (a)(1) of this section:

(1) A plain-language description of each shoppable service.

(2) An indicator when one or more of the CMS-specified shoppable services are not offered by the hospital.

(3) The payer-specific negotiated charge that applies to each shoppable service (and to each ancillary service, as applicable). Each list of payer-specific negotiated charges must be clearly associated with the name of the third party payer and plan.

(4) The discounted cash price that applies to each shoppable service (and corresponding ancillary services, as applicable). If the hospital does not offer a discounted cash price for one or more shoppable services (or corresponding ancillary services), the hospital must list its undiscounted gross charge for the shoppable service (and corresponding ancillary services, as applicable).

(5) The de-identified minimum negotiated charge that applies to each shoppable service (and to each corresponding ancillary service, as applicable).

(6) The de-identified maximum negotiated charge that applies to each shoppable service (and to each corresponding ancillary service, as applicable).

(7) The location at which the shoppable service is provided, including whether the standard charges identified in paragraphs (b)(3) through (6) of this section for the shoppable service apply at that location to the provision of that shoppable service in the inpatient setting, the outpatient department setting, or both.

(8) Any primary code used by the hospital for purposes of accounting or billing for the shoppable service, including, as applicable, the Current Procedural Terminology (CPT) code, the Healthcare Common Procedure Coding System (HCPCS) code, the Diagnosis Related Group (DRG), or other common service billing code.

(c) *Format.* A hospital has discretion to choose a format for making public the information described in paragraph (b) of this section online.

(d) *Location and accessibility of online data.* (1) A hospital must select an appropriate publicly available internet location for purposes of making public the information described in paragraph (b) of this section.

(2) The information must be displayed in a prominent manner that identifies the hospital location with which the information is associated.

(3) The shoppable services information must be easily accessible, without barriers, including but not limited to ensuring the information is:

(i) Free of charge.

(ii) Accessible without having to register or establish a user account or password.

(iii) Accessible without having to submit personal identifying information (PII).

(iv) Searchable by service description, billing code, and payer.

(e) *Frequency.* The hospital must update the standard charge information described in paragraph (b) of this section at least once annually. The hospital must clearly indicate the date that the information was most recently updated.

## Subpart C—Monitoring and Penalties for Noncompliance

### § 180.70 Monitoring and enforcement.

(a) *Monitoring and assessment.* (1) CMS evaluates whether a hospital has complied with the requirements under §§ 180.40, 180.50, and 180.60.

(2) CMS may use methods to monitor and assess hospital compliance with the requirements under this part, including, but not limited to, the following, as appropriate:

(i) CMS' evaluation of complaints made by individuals or entities to CMS.

(ii) CMS review of individuals' or entities' analysis of noncompliance.

(iii) CMS audit and comprehensive review.

(iv) Requiring submission of certification by an authorized hospital official as to the accuracy and completeness of the standard charge information in the machine-readable file.

(v) Requiring submission of additional documentation as may be necessary to make a determination of hospital compliance.

(b) *Actions to address hospital noncompliance.* If CMS concludes that the hospital is noncompliant with one or more of the requirements of § 180.40, § 180.50, or § 180.60, CMS may take any of the following actions, which generally, but not necessarily, will occur in the following order:

(1) Provide a written warning notice to the hospital of the specific violation(s). CMS will require that a hospital submit an acknowledgement of receipt of the warning notice in the form and manner, and by the deadline, specified in the notice of violation issued by CMS to the hospital.

(2) Request a corrective action plan from the hospital if its noncompliance constitutes a material violation of one or more requirements, according to § 180.80.

(3) Impose a civil monetary penalty on the hospital and publicize the penalty on a CMS website according to § 180.90 if the hospital fails to respond to CMS' request to submit a corrective action plan or comply with the requirements of a corrective action plan.

(c) *Actions to address noncompliance of hospitals in health systems.* In the event CMS takes an action to address hospital noncompliance (as specified in paragraph (b) of this section) and the hospital is determined by CMS to be part of a health system, CMS may notify health system leadership of the action and may work with health system leadership to address similar deficiencies for hospitals across the health system.

(d) *Publicizing assessments, compliance actions, and outcomes.* CMS may publicize on its website information related to the following:

(1) CMS' assessment of a hospital's compliance.

(2) Any compliance action taken against a hospital, the status of such compliance action, or the outcome of such compliance action.

(3) Notifications sent to health system leadership.

[84 FR 65602, Nov. 27, 2019, as amended at 88 FR 82185, Nov. 22, 2023]

### § 180.80 Corrective action plans.

(a) *Material violations requiring a corrective action plan.* CMS determines if a hospital's noncompliance with the requirements of this part constitutes material violation(s) requiring a corrective action plan. A material violation may include, but is not limited to, the following:

(1) A hospital's failure to make public its standard charges required by § 180.40.

(2) A hospital's failure to make public its standard charges in the form and manner required under §§ 180.50 and 180.60.

(b) *Notice of violation.* CMS may request that a hospital submit a corrective action plan, specified in a notice of violation issued by CMS to a hospital.

(c) *Compliance with corrective action plan requests and corrective actions.* (1) A hospital required to submit a corrective action plan must do so, in the form and manner, and by the deadline, specified in the notice of violation issued by CMS to the hospital and must comply with the requirements of the corrective action plan.

(2) A hospital's corrective action plan must specify elements including, but not limited to:

(i) The corrective actions or processes the hospital will take to address the deficiency or deficiencies identified by CMS.

(ii) The timeframe by which the hospital will complete the corrective action.

(3) A corrective action plan is subject to CMS review and approval.

(4) After CMS' review and approval of a hospital's corrective action plan, CMS may monitor and evaluate the hospital's compliance with the corrective actions.

(d) *Noncompliance with corrective action plan requests and requirements.* (1) A hospital's failure to respond to CMS' request to submit a corrective action plan includes failure to submit a corrective action plan in the form, manner, or by the deadline, specified in a notice of violation issued by CMS to the hospital.

(2) A hospital's failure to comply with the requirements of a corrective action plan includes failure to correct violation(s) within the specified timeframes.

### § 180.90 Civil monetary penalties.

(a) *Basis for imposing civil monetary penalties.* CMS may impose a civil monetary penalty on a hospital identified as noncompliant according to § 180.70, and that fails to respond to CMS' request to submit a corrective action plan or comply with the requirements of a corrective action plan as described in § 180.80(d).

(b) *Notice of imposition of a civil monetary penalty.* (1) If CMS imposes a penalty in accordance with this part, CMS provides a written notice of imposition of a civil monetary penalty to the hospital via certified mail or another form of traceable carrier.

(2) This notice to the hospital may include, but is not limited to, the following:

(i) The basis for the hospital's noncompliance, including, but not limited to, the following:

(A) CMS' determination as to which requirement(s) the hospital has violated.

(B) The hospital's failure to respond to CMS' request to submit a corrective action plan or comply with the requirements of a corrective action plan, as described in § 180.80(d).

(ii) CMS' determination as to the effective date for the violation(s). This date is the latest date of the following:

(A) The first day the hospital is required to meet the requirements of this part.

(B) If a hospital previously met the requirements of this part but did not update the information annually as required, the date 12 months after the date of the last annual update specified in information posted by the hospital.

(C) A date determined by CMS, such as one resulting from monitoring and assessment activities specified in § 180.70, or development of a corrective action plan as specified in § 180.80.

(iii) The amount of the penalty as of the date of the notice.

(iv) A statement that a civil monetary penalty may continue to be imposed for continuing violation(s).

(v) Payment instructions.

(vi) Intent to publicize the hospital's noncompliance and CMS' determination to impose a civil monetary penalty on the hospital for noncompliance with the requirements of this part by posting the notice of imposition of a civil monetary penalty on a CMS website.

(vii) A statement of the hospital's right to a hearing according to subpart D of this part.

(viii) A statement that the hospital's failure to request a hearing within 30 calendar days of the issuance of the notice permits the imposition of the penalty, and any subsequent penalties pursuant to continuing violations, without right of appeal in accordance with § 180.110.

(3) If the civil monetary penalty is upheld, in part, by a final and binding decision according to subpart D of this part, CMS will issue a modified notice of imposition of a civil monetary penalty, to conform to the adjudicated finding.

(c) *Amount of the civil monetary penalty.* (1) CMS may impose a civil monetary penalty upon a hospital for a violation of each requirement of this part.

(2) CMS determines the daily dollar amount for a civil monetary penalty for which a hospital may be subject as follows:

(i) For each day during Calendar Year 2021 that a hospital is determined by CMS to be out of compliance, the maximum daily dollar amount for a civil monetary penalty to which the hospital may be subject is $300. Even if the hospital is in violation of multiple discrete requirements of this part, the maximum total sum that a single hospital may be assessed per day is $300.

(ii) Beginning January 1, 2022, for each day a hospital is determined by CMS to be out of compliance:

(A) For a hospital with a number of beds equal to or less than 30, the maximum daily dollar civil monetary penalty amount to which it may be subject is $300, even if the hospital is in violation of multiple discrete requirements of this part.

(B) For a hospital with at least 31 and up to and including 550 beds, the maximum daily dollar civil monetary penalty amount to which it may be subject is the number of beds times $10, even if the hospital is in violation of multiple discrete requirements of this part.

(C) For a hospital with a number of beds greater than 550, the maximum daily dollar civil monetary penalty amount to which it may be subject is $5,500, even if the hospital is in violation of multiple discrete requirements of this part.

(D)(*1*) CMS will use the most recently available, finalized Medicare hospital cost report to determine the number of beds for a Medicare-enrolled hospital, for purposes of determining the maximum daily dollar civil monetary penalty amount under paragraph (c)(2) of this section.

(*2*) If the number of beds for the hospital cannot be determined according to paragraph (c)(2)(ii)(D)(*1*) of this section, CMS will request that the hospital provide documentation of its number of beds, in a form and manner and by the deadline prescribed by CMS in a written notice provided to the hospital. Should the hospital fail to provide CMS with this documentation in the prescribed form and manner, and by the specified deadline, CMS will impose on the hospital the maximum daily dollar civil monetary penalty amount according to paragraph (c)(2)(ii)(C) of this section.

(3) The amount of the civil monetary penalty will be adjusted annually using the multiplier determined by OMB for annually adjusting civil monetary penalty amounts under part 102 of this title.

(4) Except as provided in this paragraph, the amount of a civil monetary penalty is reduced by 35 percent if the hospital submits a written notice to CMS requesting to waive its right to a hearing under § 180.100 within 30-calendar days of the date of the notice of imposition of the civil monetary penalty. A hospital that receives a 35 percent reduction in a civil monetary penalty under this paragraph is not eligible to receive a 35 percent reduction for any subsequent civil monetary penalties imposed pursuant to continuing violations according to § 180.90(f) and also waives its right to appeal under § 180.100 any subsequent civil monetary penalties imposed for such continuing violations. A hospital is not eligible to request that CMS reduce the amount of a civil monetary penalty by 35 percent in accordance with this paragraph if—

(i) The hospital does not request to waive its right to a hearing in accordance with this paragraph; or

(ii) CMS imposed the CMP because the hospital failed to make public an MRF as required at § 180.40(a) or failed to make public a consumer-friendly list of standard charges as required at § 180.40(b).

(d) *Timing of payment of civil monetary penalty.* (1) A hospital that does not meet the criteria to receive a reduction to the civil monetary penalty that had been imposed upon it as set forth in paragraph (c)(4) of this section must pay the civil monetary penalty in full within 60 calendar days after the date of the notice of imposition of a civil monetary penalty from CMS under paragraph (b) of this section.

(2) A hospital that meets the criteria to receive a reduction to the civil monetary penalty that had been imposed upon it as set forth in paragraph (c)(4) of this section must pay the civil monetary penalty, as reduced in accordance with paragraph (c)(4) of this section, within 60 calendar days after the date of the notice of imposition of a civil monetary penalty from CMS under paragraph (b) of this section.

(3) In the event a hospital requests a hearing, pursuant to subpart D of this part, the hospital must pay the amount in full within 60 calendar days after the date of a final and binding decision, according to subpart D of this part, to uphold, in whole or in part, the civil monetary penalty.

(4) If the 60th calendar day described in paragraphs (d)(1) and (2) of this section is a weekend or a Federal holiday, then the timeframe is extended until the end of the next business day.

(e) *Posting of notice.* (1) CMS will post the notice of imposition of a civil monetary penalty described in paragraphs (b) and (f) of this section on a CMS website.

(2) In the event that a hospital elects to request a hearing, pursuant to subpart D of this part:

(i) CMS will indicate in its posting, under paragraph (e)(1) of this section, that the civil monetary penalty is under review.

(ii) If the civil monetary penalty is upheld, in whole, by a final and binding decision according to subpart D of this part, CMS will maintain the posting of the notice of imposition of a civil monetary penalty on a CMS website.

(iii) If the civil monetary penalty is upheld, in part, by a final and binding decision according to subpart D of this part, CMS will issue a modified notice of imposition of a civil monetary penalty according to paragraph (b)(3) of this section, to conform to the adjudicated finding. CMS will make this modified notice public on a CMS website.

(iv) If the civil monetary penalty is overturned in full by a final and binding decision according to subpart D of this part, CMS will remove the notice of imposition of a civil monetary penalty from a CMS website.

(f) *Continuing violations.* CMS may issue subsequent notice(s) of imposition of a civil monetary penalty, according to paragraph (b) of this section, that result from the same instance(s) of noncompliance.

[84 FR 65602, Nov. 27, 2019, as amended at 86 FR 63998, Nov. 16, 2021; 88 FR 82185, Nov. 22, 2023; 90 FR 54088, Nov. 25, 2025]

## Subpart D—Appeals of Civil Monetary Penalties

### § 180.100 Appeal of penalty.

(a) A hospital upon which CMS has imposed a penalty under this part may appeal that penalty in accordance with subpart D of part 150 of this title, except as specified in paragraph (b) of this section.

(b) For purposes of applying subpart D of part 150 of this title to appeals of civil monetary penalties under this part:

(1) Civil money penalty means a civil monetary penalty according to § 180.90.

(2) Respondent means a hospital that received a notice of imposition of a civil monetary penalty according to § 180.90(b).

(3) References to a notice of assessment or proposed assessment, or notice of proposed determination of civil monetary penalties, are considered to be references to the notice of imposition of a civil monetary penalty specified in § 180.90(b).

(4) Under § 150.417(b) of this title, in deciding whether the amount of a civil money penalty is reasonable, the ALJ may only consider evidence of record relating to the following:

(i) The hospital's posting(s) of its standard charges, if available.

(ii) Material the hospital timely previously submitted to CMS (including with respect to corrective actions and corrective action plans).

(iii) Material CMS used to monitor and assess the hospital's compliance according to § 180.70(a)(2).

(5) The ALJ's consideration of evidence of acts other than those at issue in the instant case under § 150.445(g) of this title does not apply.

### § 180.110 Failure to request a hearing.

(a) If a hospital does not request a hearing within 30 calendar days of the issuance of the notice of imposition of a civil monetary penalty described in § 180.90(b), CMS may impose the civil monetary penalty indicated in such notice and may impose additional penalties pursuant to continuing violations according to § 180.90(f) without right of appeal in accordance with this part.

(1) If the 30th calendar day described in this paragraph (a) is a weekend or a Federal holiday, then the timeframe is extended until the end of the next business day.

(2) [Reserved]

(b) The hospital has no right to appeal a penalty with respect to which it has not requested a hearing in accordance with § 150.405 of this title, unless the hospital can show good cause, as determined at § 150.405(b) of this title, for failing to timely exercise its right to a hearing.
