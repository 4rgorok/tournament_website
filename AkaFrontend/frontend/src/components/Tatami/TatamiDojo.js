import React, { useState, useEffect } from 'react';
import axios from 'axios';

import './TatamiDojo.css';

const TatamiDojo = ({ id, color, fight, type }) => {
    const [dojo, setItems] = useState([]);

    useEffect(() => {
        if(fight > 0){
            axios.get('http://localhost:8000/api/dojo', {
                params: {fid: fight, type: type},
            }
            )
            .then(response => setItems(response.data))
            .catch(error => console.error('Error fetching data:', error));
        }
        else{
            axios.get('http://localhost:8000/api/dojo', {
                params: {uid: id},
            }
            )
                .then(response => setItems(response.data))
                .catch(error => console.error('Error fetching data:', error));
        }
    }, []);
    return (
        <div style={{ color: color}}>
            {dojo.map(doj => (
                <h3 className='dojo' key={doj.id}>{doj.dojoname}</h3>
            ))}
        </div>
    );
};

export default TatamiDojo;