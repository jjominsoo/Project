import React, { useState } from "react"
import MainBox from "../../components/MainBox"
import { selectQuestions } from "../../constants/questionList"
import Select from "../../components/question/Select/Select"
import Tree from "../../components/question/Tree/Tree"
import ControlBar from "../../components/question/ControlBar"

const Question = () => {
  const [currentQuestionIdx, setCurrentQuestionIdx] = useState(0)
  const [userPreferences, setUserPreferences] = useState([])
  const questionsCount = 6

  const controlQuestionIdx = (isNext) => {
    setCurrentQuestionIdx((prev) => (isNext ? ++prev : --prev))
  }
  const updateUserPreferences = (preferN, N) => {
    let tmp = [...userPreferences]
    tmp[N] = preferN || 0
    setUserPreferences(tmp)
  }

  return (
    <div className='flex justify-center py-20 px-20 w-full text-main'>
      <MainBox>
        <div>
          {currentQuestionIdx < selectQuestions.length ? (
            <>
              <Select
                currentQuestionIdx={currentQuestionIdx}
                updateUserPreferences={updateUserPreferences}
                userPreferences={userPreferences}
              />
              <ControlBar
                userPreferences={userPreferences}
                currentQuestionIdx={currentQuestionIdx}
                controlQuestionIdx={controlQuestionIdx}
                length={questionsCount}
              />
            </>
          ) : (
            <Tree
              currentQuestionIdx={currentQuestionIdx}
              updateUserPreferences={updateUserPreferences}
              userPreferences={userPreferences}
              questionsCount={questionsCount}
              setCurrentQuestionIdx={setCurrentQuestionIdx}
            />
          )}
        </div>
      </MainBox>
    </div>
  )
}

export default Question
