# knowledge_area_context

This module is a description of the detail of the Knowledge Areas, including details related to people, processes and technology. This module is based off the SIPOC diagram used for product management (Suppliers. Inputs. Processes. Outputs. and Consumers) Context Diagrams put actifities at the center, since they produce the deliverables that meet the requirements of stakeholders. 

## Dependencies

This is a `Python 3` package with the following python package dependencies.

* `pandas`
* `os`
* `jinja2`
* `re`

## Usage

## Inputs

This package employes structured Excel file inputs to make it easy for a user to experiment configurations.

#### `knowledge_area_context_xlsx.xlsx`

This file maps to the Knowledge area context form in a structered and repeatable method. It consists of the following columns:

  * `Definition`. This section concisely defines the Knowledge Area.
  * `Goals`. This describes the purpose the Knowledge Area and the fundamental principles that guide performance of acticities within each Knowledge Area.
  * `Activities`. The activities are the actions and tasks required to meet the goals of the Knowledge Area. Some activitiesare described in terms of sub-activities, tasks, and steps. Activites are classified into four categories: Plan, Develop, Operate, and Control.
    * `(P) Planning Activities` Strategic and tactical course for meeting data management goals. Planning acticities occur on a recurring basis.
    * `(D) Development Activities` Organized around the system development lifecycle (SDLC) (analysis, design, build,test, preparation, and deployment).
    * `(C) Control Activities` Ensure the onging quality of data and the integrity, reliavility, and security of systems though which data is accessed and used.
    * `(O) Operational Activities` Support the use, maintenance, and enhancement of systems and processes through which data is accessed and used.
  * `Inputs`. The Tangible things that each Knowledge Area requires to initiate its activites. Many activities require the same inputs.
  * `Deliverables`. The outputs of the activities within the Knowledge Area, the tangible things that each function is responsible for producting. Deliverables are created buy multiple functions. 
  * `Suppliers`. The people responsible for providing or enabling or enabling access to inputs for the activities. 
  * `Consumers`. Those that directly benefit from the primary deliverables created by the data management activities.
  * `Participants`. The people that perform, manage the performance of, or approve the activities in the Knowledge Area.
  * `Tools`. The Applications nd other technologies that enable the goals of the Knowledge Area.
  * `Techniques`. The methods and procedures used to perform activities and produce deliverables within a Knowledge Area. Techniques include common coventions, best practic recommendations, standards and protocols, and, where applicable,energing alternative approaches. 
  * `Metrics`. The standards for measurement or evaluation of performance, progress, quality, effciency, or other effect. The metrics sections identify measurable facets of the work that is done within each Knowledge Area. Metrics may also measure more abstract characteristics, like improvement or value. 
