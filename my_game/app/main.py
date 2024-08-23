import olem
from top_sensor_rising_edge import TopSensorRisingEdge
import command_parser

edge_trigger = TopSensorRisingEdge()

while not edge_trigger.rising_edge_occured():
    
    msg = olem.gmsg_wait_for_message()
    command_parser.parse_msg(msg)

    olem.delay_ms(100)