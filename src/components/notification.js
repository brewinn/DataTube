import styled from 'styled-components';

const StyledNotification = styled.div`
display: block;
float: left;
margin:2%;
min-width: 20%;
max-width: 300px;
min-height: 150px;
background-color: coral;
border: solid;
margin-bottom: 5px;
`
const Notification = ({ message }) => {
  if (message === null) {
    return null
  }

  return (
    <StyledNotification className="error">
      {message}
    </StyledNotification>
  )
}

export default Notification