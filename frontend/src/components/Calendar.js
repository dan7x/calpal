import React, { useCallback } from 'react';
import { useState } from 'react';
import { Calendar, momentLocalizer } from 'react-big-calendar';
import withDragAndDrop from "react-big-calendar/lib/addons/dragAndDrop";
import 'react-big-calendar/lib/css/react-big-calendar.css';
import PromptForm from './Prompt';
import moment from 'moment';
import {
  StyleSheet,
  Button,
  View,
  SafeAreaView,
  Text,
  Alert,
} from 'react-native';
import "react-big-calendar/lib/addons/dragAndDrop/styles.css";
import "react-big-calendar/lib/css/react-big-calendar.css";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

const localizer = momentLocalizer(moment);
const DragAndDropCalendar = withDragAndDrop(Calendar);

function CalendarPal() {
    const [events, setEvents] = useState([
        {
            id: 7,
            title: 'Event 1',
            start: new Date(2023, 8, 20, 10, 0), // Year, Month (0-indexed), Day, Hour, Minute
            end: new Date(2023, 8, 20, 12, 0),
        },
        {
            id: 8,
            title: 'gtbtgtgb 2',
            start: new Date(2023, 8, 21, 14, 0),
            end: new Date(2023, 8, 21, 16, 0),
        },
        {
            id: 9,
            title: 'gtbtgtgb 2',
            start: new Date(2023, 8, 21, 14, 0),
            end: new Date(2023, 8, 21, 16, 0),
        },
    ]);

    const eventList = events.map((e) => (
        <div class="shadow p-3 mb-5 bg-white rounded-9" style={{margin: '30px'}}>
            <p><b>{e.title}</b></p>
            <div>
                <p>Begins:</p>
                <p>{e.start.toDateString()}</p>
                <p>Ends:</p>
                <p>{e.end.toDateString()}</p>
            </div>
        </div>
    ));

    // const eventItems = events.map( (e) => {
    //     <div class="shadow p-3 mb-5 bg-white rounded">
    //         <p>bort</p>
    //         <p><b>{e.title}</b></p>
    //         <p>{e.start} - {e.end}</p>
    //     </div>
    // });

    const moveEvent = useCallback(
        ({ event, start, end, isAllDay: droppedOnAllDaySlot = false }) => {
          const { allDay } = event
          if (!allDay && droppedOnAllDaySlot) {
            event.allDay = true
          }
    
          setEvents((prev) => {
            const existing = prev.find((ev) => ev.id === event.id) ?? {}
            const filtered = prev.filter((ev) => ev.id !== event.id)
            return [...filtered, { ...existing, start, end, allDay }]
          })
        },
        [setEvents]
    );
    
    const resizeEvent = useCallback(
        ({ event, start, end }) => {
            setEvents((prev) => {
            const existing = prev.find((ev) => ev.id === event.id) ?? {}
            const filtered = prev.filter((ev) => ev.id !== event.id)
            return [...filtered, { ...existing, start, end }]
            })
        },
        [setEvents]
    );

    return (
        <div style={{ padding: '20px' }}>
            <Row style={{ overflow: 'hidden', paddingBottom: 5 }}>
                <h1>Calendar App</h1>
            </Row>
            <Row>   
                <Col>
                    <h4>Upcoming Events:</h4>
                    <div style={{ height: '500px', overflow:'scroll'}}>
                        { eventList }
                    </div>
                </Col>
                <Col xs={9}>
                    <PromptForm setEvents={setEvents} />
                    <div style={{ height: '500px' }}>
                        <DragAndDropCalendar 
                        events={events} 
                        localizer={localizer}
                        onEventDrop={moveEvent}
                        onEventResize={resizeEvent}   
                        popup   
                        resizable 
                        // startAccessor="start" 
                        // endAccessor="end"
                        />
                    </div>
                </Col>
            </Row>
        </div>
    );
}

export default CalendarPal;
