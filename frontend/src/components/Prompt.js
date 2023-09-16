import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Form from 'react-bootstrap/Form';


function PromptForm({ setEvents }) {
    const [show, setShow] = useState(false);
    const [formPrompt, setPrompt] = useState('');
    const [formNegative, setNegative] = useState('');

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const updatePrompt = e => {
        setPrompt(e.target.value);
    }

    const updateNegative = e => {
        setNegative(e.target.value);
    }

    const handleSubmit = (event) => {
        event.preventDefault();

        console.log(formPrompt);
        console.log(formNegative);

        handleClose();

        // API call
        
        setEvents([
            {
                title: 'Event 1',
                start: new Date(2023, 8, 20, 10, 0), // Year, Month (0-indexed), Day, Hour, Minute
                end: new Date(2023, 8, 20, 12, 0),
            },
            {
                title: 'gtbtgtgb 2',
                start: new Date(2023, 8, 21, 14, 0),
                end: new Date(2023, 8, 21, 16, 0),
            },
        ]);
    };

  return (
    <>
        <Button variant="primary" onClick={handleShow}>
            Launch demo modal
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
            <Button variant="secondary" onClick={handleClose}>
                Close
            </Button>
            <Button variant="primary" type="submit">
                Save Changes
            </Button>
            </Modal.Footer>
        </Form>
      </Modal>
    </>
  );
}

export default PromptForm;
