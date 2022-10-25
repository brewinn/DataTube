import styled from 'styled-components';

const StyledVideo = styled.div`
background-color: coral;
border: solid;
margin-bottom: 5px;
min-height: 70%;
`
const StyledContainer = styled.div`
display: inline-block;
float: left;
margin:2%;
margin-top:10px;
margin-bottom:10px;
min-width: 20%;
max-width: 300px;
height: 215px;
overflow-y:scroll;
`
const StyledP = styled.p`
  max-width:${props => props.width || "300px"};
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin: 0;
  display:${props => props.display || "block"};
  margin-right:${props => props.marginRight || "0px"};
`
const Video = ({video}) => (
  <StyledContainer>
    <StyledP><a href='channel-or-video-url'><b>{video.title}</b></a></StyledP>
    <StyledVideo>
      <StyledP>
        Channel: {video.author}
      </StyledP>
      <StyledP display="inline" marginRight="20px" width='130px'>views: ##</StyledP>
      <StyledP display="inline" width='150px'>duration: ##:##</StyledP>
      <StyledP>Description:Go ‘beyond the nutshell’ at https://brilliant.org/nutshell by diving deeper into these topics and more with 20% off an annual subscription!This video was</StyledP>
    </StyledVideo>
    <div>
      <StyledP display="inline" marginRight="20px" width='130px'>Likes:12k</StyledP>
      <StyledP display="inline" width='150px'>10/24/2022</StyledP>
    </div>
  </StyledContainer>
)

export default Video