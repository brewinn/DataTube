import axios from 'axios'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

const getCRSF = async () => {
  const request = await axios.get('')
  console.log(request)
}

const loadPage = async (props) => 
{
  const dic = {
  'Views Ascending': 'VA',
  'Views Descending': 'VD',
  'Likes Ascending': 'LA',
  'Likes Descending': 'LD',
  'Dislikes Ascending': 'DA',
  'Dislikes Descending': 'DD',
  'Comments Ascending': 'CA',
  'Comments Descending': 'CD',
  }
  const d = props[0]+`--search_title=${(props[1] ? 'True' : 'False')}&search_description=${(props[3] ? 'True' : 'False')}&search_tags=${(props[2] ? 'True' : 'False')}&full_text_search=${(props[4] ? 'True' : 'False')}&sort_by=${dic[props[5]]}--`
  const newObject = new FormData()
  newObject.append('search_text', d)
  newObject.append('search_title', props[1] ? 'True' : 'False')
  newObject.append('search_description', props[3] ? 'True' : 'False')
  newObject.append('search_tags', props[2] ? 'True' : 'False')
  newObject.append('full_text_search', props[4] ? 'True' : 'False')
  newObject.append('sort_by', dic[props[5]])
  newObject.append('react','on')
  const response = await axios.post('', newObject)
  return response.data
}
const getChannel = async (text) =>{
  const newObject = new FormData()
  newObject.append('search_text', text)
  newObject.append('search_title', 'on')
  newObject.append('react','on')
  const st = 'channel/'+text+'r45'
  const response = await axios.get(st)
  return response.data
}

export default { loadPage, getCRSF , getChannel}