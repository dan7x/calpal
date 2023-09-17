import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Form from 'react-bootstrap/Form';
import Spinner from 'react-bootstrap/Spinner';
import moment from 'moment';
import 'moment-timezone';


const API_CALLS = "http://127.0.0.1:5001";


function PromptForm({ setEvents }) {
    const [show, setShow] = useState(false);
    const [formPrompt, setPrompt] = useState('');
    const [formNegative, setNegative] = useState('');

    const [buttonBusy, setBBusy] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const updatePrompt = e => {
        setPrompt(e.target.value);
    }

    const updateNegative = e => {
        setNegative(e.target.value);
    }

    const refreshCalendar = () => {
        let getRequestOptions = {
            method: 'GET',
            headers: {
                'Accept': 'application/json', 
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': true}
        };

        fetch(API_CALLS + '/get', getRequestOptions)
        .then(response => response.json())
        .then(data => {
            console.log("completed get. here's ur data:");
            console.log(data);

            let evload = data.map((e) => (
                {   
                    id: e.id,
                    title: e.title,
                    start: moment(e.start, "YYYY-MM-DD HH:mm:ss").tz("America/New_York").toDate(),
                    end: moment(e.end, "YYYY-MM-DD HH:mm:ss").tz("America/New_York").toDate()
                }
            )
            );

            console.log(evload);
            setEvents(evload);

            handleClose();
            setBBusy(false);
        });
    }

    const handleSubmit = (event) => {
        if (buttonBusy){
            return;
        }
        setBBusy(true);

        event.preventDefault();

        console.log(formPrompt);
        console.log(formNegative);

        // API call
        let payload = {'prompt': formPrompt, 'negative': formNegative};

        let requestOptions = {
            method: 'POST',
            headers: {
                'Accept': 'application/json', 
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': true}, 
            body: JSON.stringify(payload)
        };
    
        console.log("making post call.")
        fetch(API_CALLS + '/new', requestOptions)
        .then(response => response.json())
        .then( _ => {
            console.log("completed post. doing get.");
            refreshCalendar();
        });
          

        
        //     {
        //         id: 4,
        //         title: 'Event 1',
        //         start: new Date(2023, 8, 22, 10, 0), // Year, Month (0-indexed), Day, Hour, Minute
        //         end: new Date(2023, 8, 20, 12, 0),
        //     },
        //     {
        //         id: 5,
        //         title: 'gtbtgtgb 2',
        //         start: new Date(2023, 8, 23, 14, 0),
        //         end: new Date(2023, 8, 21, 16, 0),
        //     },
        // ]);
    };

  return (
    <>
        <Button variant="primary" onClick={handleShow}>
            + Make Plans 
        </Button>

        <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
            <Modal.Title>Make plans</Modal.Title>
        </Modal.Header>

        <Form onSubmit={handleSubmit}>
            <Modal.Body>
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Tell me how I can schedule your day:</Form.Label>
                <Form.Control 
                required 
                name="prompt" 
                placeholder="Enter schedule prompt" 
                as="textarea" rows={3} 
                onChange={updatePrompt}/>
                <Form.Text className="text-muted">
                    E.g., "Every monday, schedule me a meeting in the morning, a lunch break, a 30-minute snack in the afternoon, and gaming time in the evenings."
                </Form.Text>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
                <Form.Label>Any timing restrictions I should know about?</Form.Label>
                <Form.Control 
                name="negative" 
                placeholder="Enter scheduling constraints" 
                as="textarea" rows={3} 
                onChange={updateNegative} />
                <Form.Text className="text-muted">
                    E.g., "Do not schedule anything after 8pm on Fridays."
                </Form.Text>
            </Form.Group>
            {/* <Form.Group className="mb-3" controlId="formBasicCheckbox">
                <Form.Check type="checkbox" label="Check me out" />
            </Form.Group> */}

            </Modal.Body>
            <Modal.Footer>
            <Button variant="secondary" onClick={handleClose} disabled={buttonBusy}>
                Close
            </Button>
            <Button variant="primary" type="submit" disabled={buttonBusy}>
                {buttonBusy ? <Spinner animation="border" /> : "Let's Go!"}
            </Button>
            </Modal.Footer>
        </Form>
      </Modal>
    </>
  );
}

export default PromptForm;
