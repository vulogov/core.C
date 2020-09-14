TELEMETRY_TPL="""
(deftemplate MAIN::Telemetry
    (slot ts (type FLOAT))
    (slot x  (type SYMBOL))
    (slot y  (type SYMBOL))
    (slot value)
)
"""

_tmp = {
    "Telemetry": TELEMETRY_TPL
}