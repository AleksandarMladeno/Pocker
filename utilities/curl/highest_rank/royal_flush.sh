curl --location 'http://localhost:8080/api/hand/highest-rank' \
--header 'Content-Type: application/json' \
--data '[
    {
        "value": "A",
        "suit": "C"
    },
    {
        "value": "K",
        "suit": "C"
    },
    {
        "value": "Q",
        "suit": "C"
    },
    {
        "value": "J",
        "suit": "C"
    },
    {
        "value": "10",
        "suit": "C"
    }
]'