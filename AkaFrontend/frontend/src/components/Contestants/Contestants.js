import React, { useState, useMemo, useCallback } from 'react';
import axios from 'axios';
import { BASE_URL } from "../../utils";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import './Contestants.css';


const Contestants = ({ dojo_id }) => {
    const [fighters, setFighters] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [tatamis, setItems] = useState([]);
    const [dojo, setDojo] = useState([]);

    React.useEffect(() => {
        axios.get(BASE_URL+'/api/tatami')
            .then(response => setItems(response.data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);
    React.useEffect(() => {
        axios.get(BASE_URL+'/api/dojo/'+dojo_id)
            .then(response => setDojo(response.data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);
  // Fetch all clubs on component mount
    React.useEffect(() => {
        const fetchClubs = async () => {
        setIsLoading(true);
        try {
            const response = await axios.get(BASE_URL + '/api/fighters/'+dojo_id);
            setFighters(response.data);
        } catch (error) {
            console.error('Error fetching clubs:', error);
        } finally {
            setIsLoading(false);
        }
    };
    
    fetchClubs();
  }, []);
  let active_fighters = []
  if(fighters.length > 0 && tatamis.length > 0){
    active_fighters = fighters
        .filter(fighter => fighter.opponent != -1)
        .map(fighter => (
            {...fighter, 
                tatami : fighter["entityno"][0], 
                fights_left: parseInt(fighter.orderno/10) - (tatamis.filter(tatami=>tatami.prefix == fighter["entityno"][0])[0].fightno)}))
        .sort((a, b) => a.fights_left - b.fights_left)
    return (
        <>
            <h1 className='contestants-dojo'>Nadchodzące walki {dojo.dojoname}</h1>
            <TableContainer component={Paper}>
                <Table sx={{ minWidth: 650 }} size="small" aria-label="a dense table">
                    <TableHead>
                    <TableRow>
                        <TableCell><b>Miejsce w kolejce</b></TableCell>
                        <TableCell align="left"><b>Mata i numer walki</b></TableCell>
                        <TableCell align="left"><b>Imię i nazwisko</b></TableCell>
                        <TableCell align="left"><b>Przeciwnik</b></TableCell>
                        <TableCell align="left"><b>Poziom</b></TableCell>
                    </TableRow>
                    </TableHead>
                    <TableBody>
                    {active_fighters.map((fighter) => (
                        <TableRow
                        key={fighter.id}
                        sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                        >
                        <TableCell component="th" scope="row">
                            {fighter.fights_left}
                        </TableCell>
                        <TableCell align="left">{fighter.entityno}</TableCell>
                        <TableCell align="left">{fighter.firstname} {fighter.lastname}</TableCell>
                        <TableCell align="left">{fighter.opponent == 0 ? "TBD" : fighter.opponent_name}</TableCell>
                        <TableCell align="left">{fighter.g3 == 1 ? "KAŻDY Z KAŻDYM" : fighter.level.toUpperCase()}</TableCell>
                        </TableRow>
                    ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </>
    );              
  }
  return (<></>)
  
};

export default Contestants;