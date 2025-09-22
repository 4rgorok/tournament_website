import React, { useState, useEffect } from 'react';
import { BASE_URL } from "../../utils";
import axios from 'axios';

import './TatamiContestant.css';

const TatamiContestant = ({ id, color, fight, type }) => {
    const [contestants, setItems] = useState([]);
    console.log(id, color, fight, type, "xd")
    useEffect(() => {
        if(fight > 0){
            axios.get(BASE_URL+'/api/contestant', {
                params: {fid: fight, type: type},
            }
            )
            .then(response => setItems(response.data))
            .catch(error => console.error('Error fetching data:', error));
        }
        else{
            axios.get(BASE_URL+'/api/contestant', {
                params: {id: id},
            }
            )
            .then(response => setItems(response.data))
            .catch(error => console.error('Error fetching data:', error));
    
        }
    }, []);
    console.log(contestants)
    return (
        <div style={{ color: color}}>
            {contestants.map(contestant => (
                <h3 className='contestant' key={contestant.id}>{contestant.firstname} {contestant.lastname}</h3>
            ))}
        </div>
    );
};

export default TatamiContestant;