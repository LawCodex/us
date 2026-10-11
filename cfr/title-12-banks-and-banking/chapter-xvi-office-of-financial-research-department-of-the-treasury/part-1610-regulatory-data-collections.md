---
title: "12 CFR Part 1610 — REGULATORY DATA COLLECTIONS"
identifier: "12 CFR Part 1610"
type: regulation
jurisdiction: us
language: en
last_amended: 2026-10-02  # latest amendment date of the CFR title
status: in_force
source: "https://www.ecfr.gov/current/title-12/part-1610"
retrieved: 2026-10-11
ecfr_bulk_modified: "06-Oct-2026 21:51"
---

*Title 12—Banks and Banking › CHAPTER XVI—OFFICE OF FINANCIAL RESEARCH, DEPARTMENT OF THE TREASURY*

# PART 1610—REGULATORY DATA COLLECTIONS

**Authority:** 12 U.S.C. 5343 and 5344.

**Source:** 84 FR 4984, Feb. 20, 2019, unless otherwise noted.

## Subpart A—Collections Generally

### § 1610.1 General authority.

The collections under this part are made pursuant to the authority contained in 12 U.S.C. 5343(a) and (c)(1) and 5344(b).

### § 1610.2 General definitions.

*Council* means the Financial Stability Oversight Council.

*Legal Entity Identifier* or LEI for an entity means the global legal entity identifier maintained for such entity by a utility accredited by the Global LEI Foundation or by a utility endorsed by the Regulatory Oversight Committee that satisfies the standards implemented by the Global LEI Foundation. As used in this definition:

(1) Regulatory Oversight Committee means the Regulatory Oversight Committee (of the Global LEI System), whose charter was set forth by the Finance Ministers and Central Bank Governors of the Group of Twenty and the Financial Stability Board, or any successor thereof; and

(2) Global LEI Foundation means the not-for-profit organization organized under Swiss law by the Financial Stability Board in 2014, or any successor thereof.

*Office* means the U.S. Department of the Treasury's Office of Financial Research.

### § 1610.3 Treatment of collected information.

The Office will treat any financial transaction data or position data submitted to the Data Center under this part in accordance with the relevant provisions of law, including 12 U.S.C. 5343(b) and 5344(b).

### §§ 1610.4-1610.9 [Reserved]

## Subpart B—Specific Collections

### § 1610.10 Centrally cleared repurchase agreement data.

(a) *Definitions.*

*Central counterparty* means a clearing agency that interposes itself between the counterparties to transactions, acting functionally as the buyer to every seller and the seller to every buyer.

*Clearing agency* has the same meaning as set forth in 15 U.S.C. 78c(a)(23).

*Covered reporter* means any central counterparty for repurchase agreement transactions that meets the criteria set forth in paragraph (b)(2) of this section; provided, however, that any covered reporter shall cease to be a covered reporter only if it does not meet the dollar threshold specified in paragraph (b)(2) for at least four consecutive calendar quarters.

*General collateral trade* means a repurchase agreement transaction in which the trade reported to the central counterparty is for a category of securities as opposed to a specific security.

*Repurchase agreement transaction* or transaction means an agreement of a counterparty to transfer securities to another counterparty in exchange for the receipt of cash, and the simultaneous agreement of the former counterparty to later reacquire the same securities (or any subsequently substituted securities) from that same counterparty in exchange for the payment of cash; or an agreement of a counterparty to acquire securities from another counterparty in exchange for the payment of cash, and the simultaneous agreement of the former party to later transfer back the same securities (or any subsequently substituted securities) to the latter counterparty in exchange for the receipt of cash.

*Specific-security trade* means a repurchase agreement transaction where the trade as reported to the central counterparty is for a mutually agreed upon specific security.

(b) *Purpose and scope*—(1) *Purpose.* The purpose of this data collection is to require the reporting of certain information to the Office about repurchase agreement transactions cleared through a central counterparty. The information will be used by the Office to support the Council and Council member agencies by facilitating financial stability monitoring including research consistent with support of the Council and its member agencies, and to support the calculation of certain reference rates.

(2) *Scope of application.* Reporting under this Section is required by any central counterparty for repurchase agreement transactions that meets the definition of financial company set forth in 12 U.S.C. 5341(2) and whose average daily total open commitments in repurchase agreement contracts (gross cash positions prior to netting) across all services over all business days during the prior calendar quarter is at least $50 billion.

(c) *Data required.* (1) Covered reporters shall report trade and collateral information on all repurchase agreement transactions cleared through any of its services, subject to paragraph (c)(2) of this section, in accordance with the prescribed reporting format in this section.

(2) Covered reporters shall only report trade and collateral information with respect to any repurchase agreement transaction for which there is a current or future delivery obligation as of the file observation date, including forward-starting transactions.

(3) Covered reporters shall submit the following data elements for all general collateral trades:

Table 1 to § 1610.10**(c)**—General Collateral Trades

| Data element | Explanation |
|---|---|
| File Observation Date | The observation date of the file (typically one business day before the day the file is submitted). |
| Covered Reporter LEI | The Legal Entity Identifier of the covered reporter. |
| Transaction ID | Respondent-generated unique transaction identifier. |
| Submission Timestamp | Time that trade is first submitted to clearing service. |
| Match Timestamp | Time that trade is matched by clearing service. |
| Securities Asset Class Identifier Value | Asset class identifier. |
| Securities Asset Class Identifier Type | Type of securities identifier used (the numbering system to which the identifier belongs). |
| Cash Provider LEI | The Legal Entity Identifier of the cash provider. |
| Cash Provider Name | The legal name of the cash provider. |
| Cash Provider Internal Identifier | The internal identifier assigned by the covered reporter to the cash provider. |
| Cash Provider Direct Clearing Member LEI | The Legal Entity Identifier of the direct clearing member through which the cash provider accessed the clearing service. |
| Cash Provider Direct Clearing Member Name | The legal name of the of the direct clearing member through which the cash provider accessed the clearing service. |
| Cash Provider Direct Clearing Member Internal Identifier | The internal identifier assigned by the covered reporter to the direct clearing member through which the cash provider accessed the clearing service. |
| Securities Provider LEI | The Legal Entity Identifier of the securities provider. |
| Securities Provider Name | The legal name of the securities provider. |
| Securities Provider Internal Identifier | The internal identifier assigned by the covered reporter to the securities provider. |
| Securities Provider Direct Clearing Member LEI | The Legal Entity Identifier of the direct clearing member through which the securities provider accessed the clearing service. |
| Securities Provider Direct Clearing Member Name | The legal name of the direct clearing member through which the securities provider accessed the clearing service. |
| Securities Provider Direct Clearing Member Internal Identifier | The internal identifier assigned by the covered reporter to the direct clearing member through which the securities provider accessed the clearing service. |
| Broker LEI | The Legal Entity Identifier of the broker. |
| Broker Name | The legal name of the broker. |
| Broker Internal Identifier | The internal identifier assigned by the covered reporter to the broker. |
| Start Date | The start date of the repurchase agreement. |
| End Date | The date the repurchase agreement matures. |
| Rate | The repurchase agreement rate, expressed as an annual percentage rate on an actual/360-day basis. |
| Principal | The amount of cash borrowed or lent. |
| Optionality | The type of optionality, if any, in the repurchase agreement. |
| Minimum Maturity | The earliest possible date on which the transaction could end in accordance with its contractual terms (taking into account optionality). |

(4) Covered reporters shall submit the following data elements on the collateral delivered against net general collateral exposures for all general collateral trades:

Table 2 to § 1610.10**(c)**—General Collateral Net Exposure

| Data element | Explanation |
|---|---|
| File Observation Date | The observation date of the file (typically one business day before the day the file is submitted). |
| Covered Reporter LEI | The Legal Entity Identifier of the covered reporter. |
| Direct Clearing Member LEI | The Legal Entity Identifier of the direct clearing member of the clearing service. |
| Direct Clearing Member Name | The legal name of the direct clearing member. |
| Direct Clearing Member Internal Identifier | The internal identifier assigned by the covered reporter to the direct clearing member. |
| Transaction Side | Indicates the side of the transaction: Collateral was received by or delivered from the covered reporter. |
| Securities Identifier Value | Identifier of securities transferred. |
| Securities Identifier Type | Type of securities identifier used (the numbering system to which the identifier belongs). |
| Securities Quantity | Par value or quantity (as applicable) of securities transferred. |
| Securities Value | The market value as of most recent valuation of securities transferred, including accrued interest. |

(5) Covered reporters shall submit the following data elements for all specific-security trades:

Table 3 to § 1610.10**(c)**—Specific-Security Trades

| Data element | Explanation |
|---|---|
| File Observation Date | The observation date of the file (typically one business day before the day the file is submitted). |
| Covered Reporter LEI | The Legal Entity Identifier of the covered reporter. |
| Transaction ID | Respondent-generated unique transaction identifier. |
| Cash Provider LEI | The Legal Entity Identifier of the cash provider. |
| Cash Provider Name | The legal name of the cash provider. |
| Cash Provider Internal Identifier | The internal identifier assigned by the covered reporter to the cash provider. |
| Cash Provider Direct Clearing Member LEI | The Legal Entity Identifier of the direct clearing member through which the cash provider accessed the clearing service. |
| Cash Provider Direct Clearing Member Name | The legal name of the of the direct clearing member through which the cash provider accessed the clearing service. |
| Cash Provider Direct Clearing Member Internal Identifier | The internal identifier assigned by the covered reporter to the direct clearing member through which the cash provider accessed the clearing service. |
| Securities Provider LEI | The Legal Entity Identifier of the securities provider. |
| Securities Provider Name | The legal name of the securities provider. |
| Securities Provider Internal Identifier | The internal identifier assigned by the covered reporter to the securities provider. |
| Securities Provider Direct Clearing Member LEI | The Legal Entity Identifier of the direct clearing member through which the securities provider accessed the clearing service. |
| Securities Provider Direct Clearing Member Name | The legal name of the direct clearing member through which the securities provider accessed the clearing service. |
| Securities Provider Direct Clearing Member Internal Identifier | The internal identifier assigned by the covered reporter to the direct clearing member through which the securities provider accessed the clearing service. |
| Broker LEI | The Legal Entity Identifier of the broker. |
| Broker Name | The legal name of the broker. |
| Broker Internal Identifier | The internal identifier assigned by the covered reporter to the broker. |
| Submission Timestamp | Time that trade is first submitted to clearing service. |
| Match Timestamp | Time that trade is matched by clearing service. |
| Start Date | The start date of the repurchase agreement. |
| End Date | The date when the repurchase agreement matures; the close leg settlement date. |
| Optionality | The type of optionality, if any. |
| Minimum Maturity | The earliest possible date on which the transaction could end in accordance with its contractual terms (taking into account optionality). |
| Security Identifier Value | Identifier of pledged security. |
| Securities Identifier Type | Type of securities identifier used (the numbering system to which the identifier belongs). |
| Securities Quantity | Par value or quantity (as applicable) of securities transferred. |
| Substitution Collateral Identifier Value | Asset class identifier or no substitution. |
| Substitution Collateral Identifier Type | Type of securities identifier used (the numbering system to which the identifier belongs). |
| Cash Provider Start Leg Amount | The amount of cash transferred by the cash provider on the open leg of the transaction. |
| Securities Provider Start Leg Amount | The amount of cash received by the securities provider on the open leg of the transaction. |
| Cash Provider Rate | The rate of interest received by the cash provider, expressed as an annual percentage rate on an actual/360-day basis. |
| Securities Provider Rate | The rate of interest paid by the securities provider, expressed as an annual percentage rate on an actual/360-day basis. |
| Cash Provider Close Leg Settlement Amount | The amount of cash received by the cash provider on the close leg of the transaction. |
| Securities Provider Close Leg Settlement Amount | The amount of cash paid by the securities provider on the close leg of the transaction. |

(d) *Reporting process and collection agent.* The Office may designate a collection agent for the data reporting. Covered reporters shall submit the required data for each business day by 6:00 a.m. Eastern time on the following business day.

(e) *Compliance.* (1) Any central counterparty that is a covered reporter as of the effective date of this Section shall comply with the reporting requirements pursuant to this Section in the following manner:

(i) Subject to paragraph (e)(1)(iii) of this section, a covered reporter shall begin reporting all data elements required to be submitted pursuant to paragraph (c)(5) of this section within 180 days after April 22, 2019.

(ii) Subject to paragraph (e)(1)(iii) of this section, a covered reporter shall begin reporting all data elements required to be submitted pursuant to paragraphs (c)(3) and (4) of this section within 240 days after April 22, 2019.

(iii) If a covered reporter is able to effect a rulemaking through the Securities and Exchange Commission requiring each direct clearing member, counterparty, and broker associated with a repurchase agreement transaction to obtain an LEI and provide it to the covered reporter, the covered reporter shall begin reporting all data elements requiring an LEI other than its own pursuant to paragraphs (c)(3) through (5) of this section by the later of the effective date of its rulemaking, or 420 days April 22, 2019, and continue to report all data elements requiring a legal name or internal identifier until 365 days after the date the covered reporter begins reporting all data elements requiring an LEI pursuant to this section. If a covered reporter is unable to effect such a rulemaking, the covered reporter is not required to report any data elements requiring an LEI other than its own pursuant to paragraphs (c)(3) through (5) of this section, except, if available, the LEI for any direct clearing member, counterparty, or broker associated with a repurchase agreement transaction that has an LEI, and shall report all data elements requiring a legal name or internal identifier in any report submitted under this section regardless of whether the relevant entity has an LEI. A covered reporter shall report its own LEI in accordance with the schedules set forth in paragraphs (e)(1)(i) and (ii) of this section.

(2) The first submission by any central counterparty that is a covered reporter as of the effective date of this Section shall be submitted on the first business day after the applicable compliance date under paragraph (e)(1) of this section.

**Note 1 to paragraph (**e**)(2):**

For example, if this section became effective on March 20, 2019, a central counterparty that meets the dollar threshold specified in paragraph (b)(2) of this section for the calendar quarter ending December 31, 2018, would be required to submit its first report under paragraph (e)(1)(i) of this section on the first business day after September 16, 2019, its first report under paragraph (e)(1)(ii) of this section on November 15, 2019, and its first report with data elements requiring an LEI (other than that of the covered reporter) on May 13, 2020 (if the covered reporter effected the rulemaking described in paragraph (e)(1)(iii) of this section).

(3) Any central counterparty that becomes a covered reporter after the effective date of this Section shall comply with the reporting requirements pursuant to this Section beginning on the later of the schedule set forth in paragraphs (e)(1)(i) through (iii) of this section or the first business day of the third calendar quarter following the calendar quarter in which such central counterparty meets the dollar threshold specified in paragraph (b)(2) of this section.

**Note 2 to paragraph (**e**)(3):**

For example, if this section became effective on March 20, 2019, a central counterparty that first meets the dollar threshold specified in paragraph (b)(2) of this section for the calendar quarter ending June 30, 2019, would be required to submit its first report under paragraphs (e)(1)(i) and (ii) of this section on January 2, 2020, and its first report with data elements requiring an LEI (other than that of the covered reporter) on May 13, 2020 (if the covered reporter effected the rulemaking described in paragraph (e)(1)(iii) of this section by May 13, 2020).

**Note 3 to paragraph (**e**)(3):**

For example, if this section became effective on March 20, 2019, a central counterparty that first met the dollar threshold specified in paragraph (b)(2) for the calendar quarter ending June 30, 2020, would be required to comply with all of the reporting requirements under this section on January 2, 2021 (and would continue to be required to report all data elements requiring a legal name or internal identifier for at least 365 days after the effective date of the covered reporter's rulemaking described in paragraph (e)(1)(iii) if such effective date occurred after January 2, 2021).

### § 1610.11 Non-centrally Cleared Bilateral Repurchase Agreement Data.

(a) *Definitions.* The terms used in this section have the following meanings:

*Business day* is the period beginning at 6 p.m. Eastern Time on any day that the Fedwire Funds Service is open to 6 p.m. Eastern Time on the next day that the Fedwire Funds Service is open.

*Covered reporter* means any financial company that meets the criteria set forth in paragraph (b)(2) of this section; provided, however, that any covered reporter shall cease to be a covered reporter only if it does not meet the dollar thresholds specified in paragraph (b)(2) of this section for at least four consecutive calendar quarters.

*File observation date* means the date on which any business day ends.

*Financial company* has the same meaning as in 12 U.S.C. 5341(2).

*Government securities broker* means any financial company registered as a government securities broker under the Securities Exchange Act of 1934.

*Government securities dealer* means any financial company registered as a government securities dealer under the Securities Exchange Act of 1934.

*Investment adviser* means any financial company registered as an investment adviser with the Securities and Exchange Commission under the Investment Advisers Act of 1940.

*Non-centrally cleared bilateral repurchase agreement transaction* means an agreement of one party to sell securities to a second party in exchange for the receipt of cash, and the simultaneous agreement of the former party to later reacquire the same securities (or any subsequently substituted securities) from that same second party in exchange for the payment of cash; or an agreement of a party to acquire securities from a second party in exchange for the payment of cash, and the simultaneous agreement of the former party to later transfer back the same securities (or any subsequently substituted securities) to the latter party in exchange for the receipt of cash. The agreement does not involve a tri-party custodian and is not cleared with a central counterparty. This definition includes, but is not limited to, transactions that are executed under a Master Repurchase Agreement (MRA) or Global Master Repurchase Agreement (GMRA), or which are agreed to by the parties as subject to the provisions of 11 U.S.C. 559. Notwithstanding the above, transactions conducted under a Securities Lending Agreement (SLA) or a Master Securities Lending Agreement (MSLA) are not considered repurchase agreements, nor are repurchase agreements arising from either participation in a commercial mortgage loan or the initial securitization of a residential mortgage loan.

*Outstanding commitment* means the amount of financial obligations entered into pursuant to any repurchase agreement that opens on any business day or is outstanding as of the end of any business day, including transactions which both opened and closed on the same business day. These financial obligations include all of those that exist prior to netting.

*Securities broker* means any financial company registered as a broker with the Securities and Exchange Commission under the Securities Exchange Act of 1934.

*Securities dealer* means any financial company registered as a dealer with the Securities and Exchange Commission under the Securities Exchange Act of 1934.

(b) *Purpose and scope*—(1) *Purpose.* The purpose of this data collection is to require the reporting of certain information to the Office about non-centrally cleared bilateral repurchase agreement transactions. The information will be used by the Office to fulfill its responsibilities under Title I of the Dodd-Frank Wall Street Reform and Consumer Protection Act, including support of the Council and Council member agencies by facilitating financial stability monitoring and research consistent with support of the Council and its member agencies.

(2) *Scope of application.* Reporting under this section is required by any financial company that participates in a non-centrally cleared bilateral repurchase agreement transaction and that is:

(i) A securities broker, securities dealer, government securities broker, or government securities dealer whose average daily outstanding commitments to borrow cash and extend guarantees in non-centrally cleared bilateral repurchase agreement transactions with counterparties over all business days during the prior calendar quarter is at least $10 billion, or

(ii) Any other financial company with over $1 billion in assets or assets under management whose average daily outstanding commitments to borrow cash and extend guarantees in non-centrally cleared bilateral repurchase agreement transactions, including commitments of all funds for which the company serves as an investment adviser, with counterparties that are not securities brokers, securities dealers, government securities brokers, or government securities dealers over all business days during the prior calendar quarter is at least $10 billion.

(c) *Data required.* (1) Covered reporters shall report trade and collateral information on all non-centrally cleared bilateral repurchase agreement transactions, subject to paragraph (c)(2) of this section, in accordance with the prescribed reporting format in this section.

(2) Covered reporters shall only report trade and collateral information with respect to any non-centrally cleared bilateral repurchase agreement transaction which opens on, or is outstanding at any time during the business day, including transactions which both opened and closed during the business day.

(3) Covered reporters shall submit the following data elements for all transactions:

Table 1 to Paragraph **(c)(3)**

| Data element | Explanation |
|---|---|
| File observation date | The date on which the business day ends. |
| Covered reporter LEI | The Legal Entity Identifier of the covered reporter. |
| Cash lender LEI | The Legal Entity Identifier of the cash lender. |
| Cash lender name | The legal name of the cash lender. |
| Cash borrower name | The legal name of the cash borrower. |
| Cash borrower LEI | The Legal Entity Identifier of the cash borrower. |
| Guarantee | Indicator for whether the covered reporter issued a guarantee with respect to the transaction. |
| Transaction ID | The covered reporter-generated unique transaction identifier in an alphanumeric string format. |
| Unique transaction ID | If available, the Unique Transaction Identifier (UTI). |
| Trading platform | For transactions arranged using an outside vendor's platform, the provider of the platform. |
| Trade timestamp | The timestamp that the trade became an obligation of the covered reporter or the covered reporter's affiliate or subsidiary. |
| Start date | The start date of the repo. |
| End date | The date the repo matures. |
| Minimum maturity date | The earliest possible date on which the transaction could end in accordance with its contractual terms (taking into account optionality). |
| Cash lender internal identifier | The internal identifier assigned to the cash lender by the covered reporter, if the covered reporter is not the cash lender. |
| Cash borrower internal identifier | The internal identifier assigned to the cash borrower by the covered reporter, if the covered reporter is not the cash borrower. |
| Start leg amount | The amount of cash transferred to the cash borrower on the open leg of the transaction at the inception of the transaction. |
| Close leg amount | The amount of cash to be transferred by the cash borrower on the end date of the transaction. |
| Current cash amount | The amount of cash to be transferred by the cash borrower, inclusive of principal, accrued interest and other adjustments, as of the end of the business day. |
| Start leg currency | The currency which is used in the Start leg amount field. |
| Rate | The rate of interest paid by the cash borrower on the transaction, expressed as an annual percentage rate on an actual/360-day basis. |
| Floating rate benchmark | The name of the benchmark interest rate upon which the transaction is based. |
| Floating rate reset frequency | The time period, in calendar days, describing the frequency of the floating rate resets. |
| Spread | The contractual spread over (or below) the benchmark rate referenced in the repurchase agreement. |
| Securities identifier type | The identifier type for the securities transferred between cash borrower and cash lender. |
| Security identifier | The identifier of securities transferred between the cash borrower and the cash lender in the repo. |
| Securities quantity | The number of units (e.g., shares, bonds, bills, notes) transferred to the cash lender as of the end of the business day. |
| Securities value | The market value of the transferred securities as of the end of the business day, inclusive of accrued interest. |
| Securities value at inception | The market value of the transferred securities at the inception of the transaction, inclusive of accrued interest. |
| Securities value currency | The currency used in the Securities value and Securities value at inception fields. |
| Haircut | The difference between the market value of the transferred securities and the purchase price paid at the inception of the transaction. |
| Special instructions, notes, or comments | The covered reporter may characterize any detail of the transaction with special instructions, notes, or comments. |

(d) *Reporting process.* Covered reporters shall submit the required data for each business day by 11 a.m. Eastern Time on the following business day. The Office may either collect the data itself or designate a collection agent for that purpose.

(e) *Compliance date.* (1) Any financial company that meets the criteria set forth in paragraph (b)(2)(i) of this section as of July 5, 2024 shall comply with the reporting requirements pursuant to this section 150 days after July 5, 2024. Any such covered reporter's first submission shall be submitted on the first business day after such compliance date.

(2) Any financial company that meets the criteria set forth in paragraph (b)(2)(ii) of this section as of July 5, 2024 shall comply with the reporting requirements pursuant to this section 360 days after July 5, 2024. Any such covered reporter's first submission shall be submitted on the first business day after such compliance date.

(3) Any financial company not described in paragraph (e)(1) or (2) of this section that meets the criteria set forth in paragraph (b)(2)(i) of this section after July 5, 2024 shall comply with the reporting requirements pursuant to this section 150 days after the last day of the calendar quarter in which such financial company becomes a covered reporter.

(4) Any financial company not described in paragraph (e)(1) or (2) of this section that meets the criteria set forth in paragraph (b)(2)(ii) of this section after July 5, 2024 shall comply with the reporting requirements pursuant to this section 360 days after the last day of the calendar quarter in which such financial company becomes a covered reporter.

[89 FR 37107, May 6, 2024, as amended at 90 FR 14413, Apr. 2, 2025]
