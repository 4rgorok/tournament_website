import React, { useState, useEffect } from 'react';
import axios from 'axios';

import './TatamiTurniej.css';

const TatamiTurniej = () => {
    const [turniej, setItems] = useState([]);

    useEffect(() => { 
        axios.get('http://localhost:8000/api/setup')
            .then(response => setItems(response.data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);
    return (
        <div>
            {turniej.map(turn => (
                <h1 className='turniej' key={turn.id}>{turn.tournament}</h1>
            ))}
        </div>
    );
};

export default TatamiTurniej;