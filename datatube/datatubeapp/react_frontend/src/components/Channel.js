import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col'

const Channel = ({channel}) => {
  if(channel.fields)
  return(
    <>
    <Row className='text-center'>  
      <Col><h2>{channel.pk}</h2></Col>
      <Col><a href={channel.fields.channel_url}>
        <h3>{channel.fields.channel_url}</h3>
        </a></Col>
        <Col></Col>
    </Row>
    <Row className='text-center'>
      <Col><h3>Subscribers: {channel.fields.subscribers}</h3></Col>
      <Col><h3>Total Views: {channel.fields.views}</h3></Col>
      <Col><h3>Joined: {channel.fields.joined}</h3></Col>
    </Row>
    <Row>
      <Col>{channel.fields.description}</Col>
    </Row>
    <br></br>
    </>
  )
  return(
    <h2>{channel}</h2>
  )
  }

  export default Channel