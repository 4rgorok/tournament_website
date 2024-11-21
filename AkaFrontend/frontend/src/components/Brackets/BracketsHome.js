import React, { useState, useEffect } from 'react';

import './BracketsHome.css';
import axios from 'axios';

import { useWindowSize } from "@uidotdev/usehooks";
import { SingleEliminationBracket, DoubleEliminationBracket, Match, MATCH_STATES, SVGViewer } from '@g-loot/react-tournament-brackets';

export const matches = [
  {
    id: 20467,
    name: 'Semi Final - Match 2',
    nextLooserMatchId: null,
    nextMatchId: 20463,
    participants: [
      {
        id: 'b9a3cc7a-95d9-483a-b515-f24bd0531f45',
        isWinner: true,
        name: 'spacefudg3',
        resultText: 'WO',
        status: 'WALKOVER'
      },
      {
        id: '7535778a-24db-423f-928b-ca237cff67fc',
        isWinner: false,
        name: 'SeatloN',
        resultText: 'NS',
        status: 'NO_SHOW'
      }
    ],
    startTime: '2021-07-28T00:00:00.000+00:00',
    state: 'WALK_OVER',
    tournamentRoundText: '1'
  },
    {
      id: 20464,
      name: 'Semi Final - Match 1',
      nextLooserMatchId: null,
      nextMatchId: 20463,
      participants: [
        {
          id: '2137',
          isWinner: false,
          name: 'Alex',
          resultText: 'NS',
          status: 'NO_SHOW'
        },
        {
          id: 'GlootOne',
          isWinner: false,
          name: 'GlootOne',
          resultText: 'NS',
          status: 'NO_SHOW'
        }
      ],
      startTime: '2021-07-28T00:00:00.000+00:00',
      state: 'SCORE_DONE',
      tournamentRoundText: '2'
    },
    {
      id: 20465,
      name: 'Round 1 - Match 1',
      nextLooserMatchId: null,
      nextMatchId: 20464,
      participants: [
        {
          id: '1d11ce35-de11-49de-b48e-cec5427eb82c',
          isWinner: true,
          name: 'Alex',
          resultText: '1',
          status: 'PLAYED'
        },
        {
          id: 'a504c49a-e9b2-4a2e-b4b8-a2c11651c356',
          isWinner: false,
          name: 'BTC',
          resultText: '0',
          status: 'PLAYED'
        }
      ],
      startTime: '2021-07-27T23:00:00.000+00:00',
      state: 'SCORE_DONE',
      tournamentRoundText: '1'
    },
    {
      id: 20466,
      name: 'Round 1 - Match 2',
      nextLooserMatchId: null,
      nextMatchId: 20464,
      participants: [
        {
          id: 'GlootOne',
          isWinner: false,
          name: 'GlootOne',
          resultText: 'WO',
          status: null
        }
      ],
      startTime: '2021-07-27T23:00:00.000+00:00',
      state: 'WALK_OVER',
      tournamentRoundText: '1'
    },
    {
      id: 2046890,
      name: '',
      nextLooserMatchId: null,
      nextMatchId: 20467,
      participants: [
        {
          id: 'b9a3cc7a-95d9-483a-b515-f24bd0531f4590',
          isWinner: false,
          name: ' ',
          resultText: ' ',
          status: ' '
        },
        {
          id: 'b9a3cc7a-95d9-483a-b515-f24bd0531f4590',
          isWinner: false,
          name: ' ',
          resultText: ' ',
          status: ' '
        }
      ],
      startTime: '',
      state: '',
      tournamentRoundText: '1'
    },
    {
      id: 2046890,
      name: 'Round 1 - Match 3',
      nextLooserMatchId: null,
      nextMatchId: 20467,
      participants: [
        {
          id: 'b9a3cc7a-95d9-483a-b515-f24bd0531f405',
          isWinner: false,
          name: '',
          resultText: ' ',
          status: null
        }
      ],
      startTime: '2021-07-27T23:00:00.000+00:00',
      state: '',
      tournamentRoundText: '1'
    },
    {
      id: 20463,
      name: 'Final - Match',
      nextLooserMatchId: null,
      nextMatchId: null,
      participants: [
        {
          id: null,
          isWinner: false,
          name: '',
          resultText: '',
          status: 'NO_PARTY'
        },
        {
          id: 'b9a3cc7a-95d9-483a-b515-f24bd0531f45',
          isWinner: false,
          name: 'spacefudg3',
          resultText: '',
          status: null
        }
      ],
      startTime: '2021-07-28T01:00:00.000+00:00',
      state: 'DONE',
      tournamentRoundText: '3'
    }
  ]

  export const SingleElimination = () => (
    <SingleEliminationBracket
      matches={matches}
      matchComponent={Match}
      svgWrapper={({ children, ...props }) => (
        <SVGViewer
        width={2000}
        height={2000}
        background="rgb(11, 13, 19)"
        SVGBackground="rgb(11, 13, 19)"
        {...props}
      >
          {children}
        </SVGViewer>
      )}
      options={{
        style: {
          roundHeader: {
            fontColor: undefined,
            fontFamily: undefined,
          }
        }
      }}
      theme={{
        svgBackground: '#f50707',
        border: {
          color: '#22293B',
          highlightedColor: '#707582'
        },
        canvasBackground: '#0B0D13',
        disabledColor: '#5D6371',
        fontFamily: 'monospace',
        matchBackground: {
          lostColor: '#141822',
          wonColor: '#1D2232'
        },
        roundHeaders: {
          background: '#2F3648'
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
      }}
    />
  );

const Brackets = () => {
  return <SingleElimination />;
};

export default Brackets;