# LogisticAgent
This is an AI Agent project to handle customers requests that can intelligently interact with logistics API

## Setup & Installation

### 1. Prerequisites
- Python 3.10 or higher installed.
- A Google Cloud Project with Vertex AI API enabled.
- [Google Cloud CLI](https://cloud.google.com/sdk/docs/install) installed.

### 2. Create a Virtual Environment
Isolate your project dependencies by creating a virtual environment.

python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. How to Run
Option A: Web Interface
adk web agent
Option B: Terminal Mode
adk run agent

### Sample tests


## Thinking process:
### 1. First, using a single agent to handle the examples: check shippment status and create new shipment.
### 2. After reviewing the API docs, trying to use multi agent mode. Using managers to handle specilaized domain
    * Order agent to handle order related requests
    * Shipping agent to handle shipping requests
    * Tracking agent to handle tracking requests
### 3. Tracking APIs have more volume than the shipping and order's so in order to avoid too many tools for the agent, 
starting to use sub-team to split it. 
    * finance agent to handle finance related query request like currency
    * status agent to handle status query requests like pickup info, waybill info
    * carrier agent to handle carrier related query request like get channel infor
    * order and shipping specialists are used to handle create/delete/update requests for order and shipping
### 4. Polish: add error handling, edege case and retry.


## Sample test cases:
### Domain	    Test Prompt	                                                        Expected Behavior / Answer
Labels	    "Print labels for order T620200611-1001"	                Success. Should return a PDF link (http://www.cntodd.top/...).
Deletion	"Delete order T620230804212"	                            API Error Handling. Should say the deletion failed because the order is "already received" (Mock logic).
Pickup	    "Check pickup for waybill 5722916732"	                    Success. Should return driver "小聂同学呀" and status "Pending Confirmation".
Waybill	    "Find the waybill for customer number T620200611-1001"	    Success. Should return waybill 926129030293605.
Carriers	"What shipping channels do you support?"	                Success. Should list China Post, TNT, and Mason Clippers.
Currency	"What currencies do you accept?"                            Success. Should list CNY, HKG, and USD.