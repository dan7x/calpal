import React from 'react';
import { useState } from 'react';
import { Calendar, momentLocalizer } from 'react-big-calendar';
import 'react-big-calendar/lib/css/react-big-calendar.css';
import PromptForm from './components/Prompt';
import moment from 'moment';
import {
  StyleSheet,
  Button,
  View,
  SafeAreaView,
  Text,
  Alert,
} from 'react-native';
import CalendarPal from './components/Calendar';

function App() {
    
    return (
        <div className="App">
            <CalendarPal />
        </div>
    );
}

export default App;
