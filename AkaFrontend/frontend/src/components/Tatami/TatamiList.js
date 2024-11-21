import React, { useState, useEffect } from 'react';
import TatamiContestant from './TatamiContestant';
import TatamiCategory from './TatamiCategory';
import TatamiDojo from './TatamiDojo';
import TatamiTurniej from './TatamiTurniej';

import './TatamiList.css';
import axios from 'axios';

const TatamiList = () => {
    const [tatamis, setItems] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/tatami')
            .then(response => setItems(response.data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);
    
    let idcontainer = 'id' + tatamis.length

    return (
        <div className='App'>
        <TatamiTurniej/>
            <div className='flex-wrapper'>   
                <div id={idcontainer} className='tatami-container'>
                    {tatamis.filter((tatami) => tatami.isactivekumite == true).map(tatami => (
                        <div className='tatami-box' key={tatami.id}>
                            <h2 className='mata'>Mata {tatami.prefix} - kumite</h2>
                            <TatamiCategory id = {tatami.idkumitetournament} type = 'kumite'/>
                            <div className='fight'>
                                <TatamiContestant color="blue" fight={tatami.idkumitetournament} type='1'/>
                                <TatamiDojo fight={tatami.idkumitetournament} type='1' color="blue"/>
                                <p className='vs'>vs</p> 
                                <TatamiContestant color="red" fight={tatami.idkumitetournament} type='0'/>
                                <TatamiDojo fight={tatami.idkumitetournament} type='0' color="red"/>
                            </div>
                        </div>
                    ))}
                    {tatamis.filter((tatami) => tatami.isactivekata == true).map(tatami => (
                        <div className='tatami-box' key={tatami.id}>
                            <h2 className='mata'>Mata {tatami.prefix} - kata</h2>
                            <TatamiCategory id = {tatami.idcontestantkata} type = 'kata'/>
                            <div className='fight'>
                                <TatamiContestant id={tatami.idcontestantkata} color="black"/>
                                <TatamiDojo id = {tatami.idcontestantkata} color="black"/>
                            </div>
                            
                        </div>
                    ))}
                    {tatamis.filter((tatami) => tatami.isactive == false).map(tatami => (
                        <div 
                            className='tatami-box'
                            key={tatami.id}
                        >
                            <h2 className='mata'>Mata {tatami.prefix} - nieaktywna</h2>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default TatamiList;