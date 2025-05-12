export const selectQuestions = [
  {
    type: "SELECT",
    title: "What price range do you prefer?",
    list: [
      "Wines for a beginners 🐣",
      "Wines for a small party 🎉",
      "Wines for a gift 🍾",
      "Wines for myself  💵",
      "Wines for personal collection  💸",
    ],
  },
  {
    type: "SELECT",
    title: "Which country do you prefer?",
    list: [
      "France 🇫🇷",
      "Italy 🇮🇹",
      "Spain 🇪🇸",
      "Australia 🇦🇺",
      "Argentina 🇦🇷",
      "the United States 🇺🇸",
      "Etc",
    ],
  },
]

export const treeQuestions = {
  0: {
    type: "TREE",
    title: "Which wine do you prefer, red or white?",
    leafs: {
      1: "RED 🔴",
      2: "WHITE ⚪️",
    },
  },
  1: {
    type: "TREE",
    title: "Do you prefer wine with a strong fruity scent?",
    leafs: {
      3: "Yes 🙆",
      4: "No 🙅",
    },
  },
  2: {
    type: "TREE",
    title: "Do you prefer wine with a strong fruity scent?",
    leafs: {
      5: "Yes 🙆",
      6: "No 🙅",
    },
  },
  3: {
    type: "TREE",
    title: "Do you enjoy your wine with food?",
    leafs: {
      7: "Yes 🙆",
      8: "No 🙅",
    },
  },
  4: {
    type: "TREE",
    title: "Do you enjoy your wine with food?",
    leafs: {
      9: "Yes 🙆",
      10: "No 🙅",
    },
  },
  5: {
    type: "TREE",
    title: "Which of the following flavors do you prefer the most?",
    leafs: {
      11: "Sweet(달콤)",
      12: "Fesh(상콤)",
      13: "Anything",
    },
  },
  6: {
    type: "TREE",
    title: "Which of the following flavors do you prefer the most?",
    leafs: {
      14: "Creamy",
      15: "Dry",
    },
  },
}

export const QuestionsList = [selectQuestions, treeQuestions]
