import React, { useState, useEffect } from "react"
import TreeQuestion from "./TreeQuestion"
import QuestionTitle from "../QuestionTitle"
import { treeQuestions } from "../../../constants/questionList"
import ControlBar from "../ControlBar"

const Tree = ({
  userPreferences,
  currentQuestionIdx,
  updateUserPreferences,
  questionsCount,
  setCurrentQuestionIdx,
}) => {
  const [treeQuestionNode, setTreeQuestionNode] = useState(0)
  const [tmpQuestionNode, setTmpTreeQuestionNode] = useState(0)

  const changeTreeQuestionNode = (nodeN) => {
    setTmpTreeQuestionNode(nodeN)
  }
  const controlTreeQuestionIdx = (isNext) => {
    if (isNext) {
      if (!tmpQuestionNode) return
      setCurrentQuestionIdx((prev) => (isNext ? ++prev : --prev))
    } else {
      const prev = Object.keys(treeQuestions).filter(
        (key) => treeQuestions[key].leafs[treeQuestionNode]
      )
      setTmpTreeQuestionNode(prev[0])
      setCurrentQuestionIdx((prev) => (currentQuestionIdx === 1 ? 1 : --prev))
    }
  }
  useEffect(() => {
    setTreeQuestionNode(tmpQuestionNode)
  }, [currentQuestionIdx])

  return (
    <>
      <QuestionTitle title={treeQuestions[treeQuestionNode].title} />
      <TreeQuestion
        leafs={treeQuestions[treeQuestionNode].leafs}
        currentQuestionIdx={currentQuestionIdx}
        userPreferences={userPreferences}
        updateUserPreferences={updateUserPreferences}
        changeTreeQuestionNode={changeTreeQuestionNode}
      />
      <ControlBar
        userPreferences={userPreferences}
        currentQuestionIdx={currentQuestionIdx}
        controlQuestionIdx={controlTreeQuestionIdx}
        length={questionsCount}
      />
    </>
  )
}

export default Tree
