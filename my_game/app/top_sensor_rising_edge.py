import olem

class TopSensorRisingEdge:
    def __init__(self) -> None:
        self._previous_top = False

    def rising_edge_occured(self) -> bool:
        presence = olem.ir_top_is_hand_present()
        rising_edge = presence and not self._previous_top
        self._previous_top = presence

        return rising_edge
