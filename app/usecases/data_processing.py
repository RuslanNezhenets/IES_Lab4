import math

from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData


def process_agent_data(agent_data: AgentData, ) -> ProcessedAgentData:
    magnitude = math.sqrt(
        agent_data.accelerometer.x ** 2 + agent_data.accelerometer.y ** 2 + agent_data.accelerometer.z ** 2)

    if magnitude > 25000:
        road_state = "Дуже нерівне покриття"
    elif magnitude > 18000:
        road_state = "Нерівне покриття"
    else:
        road_state = "Рівне покриття"

    return ProcessedAgentData(road_state=road_state, agent_data=agent_data)
