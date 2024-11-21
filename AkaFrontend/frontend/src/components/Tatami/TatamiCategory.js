import React, { useState, useEffect } from 'react';
import axios from 'axios';

import './TatamiCategory.css';

const TatamiCategory = ({ id, type }) => {
    const [category, setItems] = useState([]);

    useEffect(() => {
        if(type == 'kata'){
            axios.get('http://localhost:8000/api/kata', {
                params: {uid: id},
            }
            )
                .then(response => setItems(response.data))
                .catch(error => console.error('Error fetching data:', error));
        
        }
        else if(type == 'kumite'){
            axios.get('http://localhost:8000/api/kumite', {
                params: {fid: id},
            }
            )
                .then(response => setItems(response.data))
                .catch(error => console.error('Error fetching data:', error));
        }
    }, []);
    if(category[0] != undefined)
    {
        return (
            <h2 className='category' key={category[0].id}>{category[0].groupname}</h2>
        );
    }
};

export default TatamiCategory;