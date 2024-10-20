
# Availability and Scalability

Using a cloud solution, there are two metrics to measure the quality of said solution on. These are availability and scalability. 

**Availability** describes the access to a cloud solution, a cloud solution must have high availability so that it can be accessed during any time. Azure guarantees continious access regardless of disruptions or other events, as part of what is known as the Service Level Agreements (SLAs). Azure uses availability as part of its SLA, Azure provides 99.9% availability as part of its SLA. Each Azure service have different SLA specifications, so it is important to take into account before designing a solution around a specific Azure service.

Another aspect is that of **Scalability**. This measure a cloud service's ability to scale according the demand. This could be an application requiring more resources or an increase in the number of applications. One benefit of scalability is that you are paying exactly for what you use, nothing less, nothing more. As when the demand goes down, you pay less. Scalability spans two dimensions, *vertical* scalability and *horizontal* scalability. 

Vertical scalability describes scalability in terms of the hardware resources dedicated to a single application, such as adding more CPUs and RAM to a virtual machine to meet the additional processing power. 

Horizontal scalability refers to scalability that occurs (manually or automatically) to meet higher demand. This could be in adding more virtual machines or containers. 

# Predictability and Reliability

