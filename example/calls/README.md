# Voice calls

This script is a simplified example that uses basic cellular
voice functionality.

Script will only work if the modem supports voice calls
and also after the modem is registered to the cellular network
and the SIM card is unlocked.

Run with sudo or change user modemmanager PolicyKit.

### The result of the script:

```
Exist calls: []                                                                                                                               │
Call list after create: ['/org/freedesktop/ModemManager1/Call/5']                                                                            │
--- Call properties ---                                                                                                                       │
State value: 0, name: MM_CALL_STATE_UNKNOWN                                                                                                  │
State reason value: 0, name: MM_CALL_STATE_REASON_UNKNOWN                                                                                    │
Direction value: 2, name: MM_CALL_DIRECTION_OUTGOING                                                                                         │
Multiparty: False                                                                                                                            │
Number: *************                                                                                                                       │
Audio port:                                                                                                                                  │
Audio format: {}                                                                                                                         │
--- Start call ---
Current call state: MM_CALL_STATE_DIALING                                                                                                    │
Current call state: MM_CALL_STATE_DIALING                                                                                                    │
Current call state: MM_CALL_STATE_DIALING                                                                                                    │
Current call state: MM_CALL_STATE_RINGING_OUT                                                                                                │
Current call state: MM_CALL_STATE_RINGING_OUT                                                                                                │
Current call state: MM_CALL_STATE_RINGING_OUT                                                                                                │
Current call state: MM_CALL_STATE_RINGING_OUT                                                                                                │
Current call state: MM_CALL_STATE_RINGING_OUT                                                                                                │
Current call state: MM_CALL_STATE_ACTIVE                                                                                                     │
Current call state: MM_CALL_STATE_ACTIVE                                                                                                     │
Current call state: MM_CALL_STATE_ACTIVE                                                                                                     │
Current call state: MM_CALL_STATE_ACTIVE                                                                                                     │
Current call state: MM_CALL_STATE_ACTIVE                                                                                                     │
Current call state: MM_CALL_STATE_TERMINATED                                                                                                 │
--- Stop call ---
Call list after delete: []
```