table = {
    "SLEEP" : {"HIT" : "WAKE"},
    "wake" : {"TIMER10", "SLEEP"}
}

cur_state = "SLEEP"
next_state = table[cur_state]["HIT"]
