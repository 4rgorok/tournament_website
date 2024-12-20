import React, { useState, useEffect } from 'react';
import { BASE_URL } from "../../utils";
import './BracketsHome.css';
import axios from 'axios';

import { useWindowSize } from "@uidotdev/usehooks";
import { SingleEliminationBracket, DoubleEliminationBracket, Match, MATCH_STATES, SVGViewer } from '@g-loot/react-tournament-brackets';

function prepare_bracket_data(bracket){
    let matches = []
    bracket.forEach(element => {
      console.log(element)
      let match = {
        id: element.fightno,
        name: '',
        nextLooserMatchId: null,
        nextMatchId: element.nextfightno,
        startTime: element.entityno,
        state: 'SCHEDULED',
        tournamentRoundText: element.leveltxt,
        participants: []
      }

      if(element.entityno[0] == ' '){
        match.state = ''
        match.participants = [
          {
            id: element.id,
            isWinner: false,
            name: ' ',
            resultText: 'D',
            status: ' '
          },
          {
            id: element.id,
            isWinner: false,
            name: ' ',
            resultText: 'D',
            status: ' '
          }
        ]
      }
      else if(element.winner != 0){
        match.state = "SCORE_DONE"
        match.participants = [
          {
            id: element.akaid,
            isWinner: element.akaid == element.winner ? true : false,
            name: 'ala ma kota ola ma psa',//element.akaid,
            resultText: element.akaid == element.winner ? 'W' : 'L',
            status: 'PLAYED'
          },
          {
            id: element.shiroid,
            isWinner: element.shiroid == element.winner ? true : false,
            name: element.shiroid,
            resultText: element.shiroid == element.winner ? 'W' : 'L',
            status: 'PLAYED'
          }
        ]
      }
      else{
        match.state = "SCHEDULED"
        if(element.akaid != 0){
          match.participants.push({
            id: element.akaid,
            isWinner: false,
            name: element.akaid,
            resultText: '',
            status: null
          })
        }
        if(element.shiroid != 0){
          match.participants.push({
            id: element.shiroid,
            isWinner: false,
            name: element.shiroid,
            resultText: '',
            status: null
          })
        }
      }
      matches.push(match)
    });
    return matches
}

export const SingleElimination = ({ matches }) => (
      <SingleEliminationBracket
        matches={matches}
        //matchComponent={Match}
        
        /*theme={{
          border: {
            color: '#22293B',
            highlightedColor: '#707582'
          },
          fontFamily: 'monospace',
          matchBackground: {
            lostColor: '#141822',
            wonColor: '#1D2232'
          },
          roundHeaders: {
            background: '#2F3648' //nagłówki poziomu rund
          },
          score: {
            background: {
              lostColor: '#10131C',
              wonColor: '#10131C'
            },
            text: {
              highlightedLostColor: '#FF9505',
              highlightedWonColor: '#118ADE'
            }
          },
          textColor: {
            dark: '#707582',
            disabled: '#5D6371',
            highlighted: '#E9EAEC',
            main: '#BEC0C6'
          },
          transitionTimingFunction: 'cubic-bezier(0, 0.92, 0.77, 0.99)'
        }}*/
        options={{
          style: {
            roundHeader: { backgroundColor: '#ff0000' },
            connectorColor: '#FF8C00',
            connectorColorHighlight: 'white',
          },
        }}
        /*svgWrapper={({ children, ...props }) => (
          <SvgViewer
            background="#FFF"
            SVGBackground="#FFF"
            width={finalWidth}
            height={finalHeight}
            {...props}
          >
            {children}
          </SvgViewer>
        )}*/
        matchComponent={({
          match,
          onMatchClick,
          onPartyClick,
          onMouseEnter,
          onMouseLeave,
          topParty,
          bottomParty,
          topWon,
          bottomWon,
          topHovered,
          bottomHovered,
          topText,
          bottomText,
          connectorColor,
          computedStyles,
          teamNameFallback,
          resultFallback,
        }) => (
          <div className={`outerMatch ${topParty.resultText == 'D' ? 'nonexistant' : 'existent'}`}>
            <div className='matchNumber'> {topText}  &nbsp;</div>
            <div
              onMouseEnter={() => onMouseEnter(topParty.id)}
              onMouseLeave={() => onMouseLeave(topParty.id)}
              className={`record aka ${topParty.resultText == 'W' ? 'win' : 'loose'}`}
            >
              <div className='outerPlayer'>{topParty.name || teamNameFallback}</div>
              <div className='outerScore'><div className='innerScore'>{topParty.resultText ?? resultFallback(topParty)}</div></div>
            </div>
            
            <div
            onLoad={eval(console.log(topText, 'cwel'))}
              onMouseEnter={() => onMouseEnter(bottomParty.id)}
              onMouseLeave={() => onMouseLeave(bottomParty.id)}
              className={`record shiro ${bottomParty.resultText == 'W' ? 'win' : 'loose'}`}
            >
              <div className='outerPlayer'>{bottomParty.name || teamNameFallback}</div>
              <div className='outerScore'><div className='innerScore'>{bottomParty.resultText ?? resultFallback(topParty)}</div></div>
            </div>
            <div> &nbsp;</div>
          </div>
          
        )}
      />
    );

const Brackets = ({ id }) => {
  const [bracket, setItems] = useState([]);
    id = 12
    useEffect(() => {
        axios.get(BASE_URL+'/api/kumitetournament', {
        params: {gid: id},
      }
      )
      .then(response => setItems(response.data))
      .catch(error => console.error('Error fetching data:', error));
 
    }, []);
  console.log(bracket)
  if(bracket[0] != undefined){
    let matches = prepare_bracket_data(bracket)
    console.log(matches)
    return <SingleElimination matches = {matches}/>;
  } 
};

export default Brackets;

/*
SELECT
    KumiteTournament.*,
    aka.FirstName AS aka_name,
    aka.LastName AS aka_surname,
    shiro.FirstName AS shiro_name,
    shiro.LastName AS shiro_surname
FROM
    KumiteTournament
LEFT OUTER JOIN
    Contestant aka ON KumiteTournament.AkaId = aka.id
LEFT OUTER JOIN
    Contestant shiro ON KumiteTournament.ShiroId = shiro.id
WHERE
	KumiteTournament.IdGroup = 12;
  */