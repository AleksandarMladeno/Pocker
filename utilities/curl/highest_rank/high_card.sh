curl --location 'http://localhost:8080/api/hand/highest-rank' \
--header 'Content-Type: application/json' \
--data '[
    {
        "value": "A",
        "suit": "S"
    },
    {
        "value": "J",
        "suit": "H"
    },
    {
        "value": "9",
        "suit": "S"
    },
    {
        "value": "K",
        "suit": "C"
    },
    {
        "value": "5",
        "suit": "S"
    }
]'