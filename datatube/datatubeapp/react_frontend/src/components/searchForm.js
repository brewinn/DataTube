import { useState } from 'react'
import Dropdown from 'react-bootstrap/Dropdown';

const SearchForm = ({ searchText, setSearchText, getData }) => {
  const [titleCheck, setTitleCheck] = useState(true);
  const [descriptionCheck, setDescriptionCheck] = useState(false);
  const [tags, setTags] = useState(false);
  const [fts, setFts] = useState(false);
  const [sort, setSort] = useState('Views Ascending')
  const handleDescriptionChange = () => {
    setDescriptionCheck(!descriptionCheck)
  }

  const handleTitleChange = () => {
    setTitleCheck(!titleCheck)
  }
  const handleTagChange = () => {
    setTags(!tags)
  }
  const handleFtsChange = () => {
    setFts(!fts)
  }
  const handleSort = (event) => {
    setSort(event.target.text)
  }
  return (
    <div className="ms-2 ps-1 mb-2">
      <p>
        Search:
      </p>
      <form onSubmit={getData}>
        <div>
          <span>
            Title
          </span>
          <input
            type="text"
            value={searchText}
            name="newTitle"
            placeholder='Video Title'
            onChange={({ target }) => setSearchText(target.value)}
          />
          <span className='mx-1'>
            Search Title
          </span>
          <input
            type="checkbox"
            checked={titleCheck}
            onChange={handleTitleChange}
          />
          <span className='mx-1'>
            Search Tags
          </span>
          <input
            type="checkbox"
            checked={tags}
            onChange={handleTagChange}
          />
          <span className='mx-1'>
            Search Description
          </span>
          <input
            type="checkbox"
            checked={descriptionCheck}
            onChange={handleDescriptionChange}
          />
          <span className='mx-1'>
            Full Text Search
          </span>
          <input
            type="checkbox"
            checked={fts}
            onChange={handleFtsChange}
          />
          <span className='mx-1'>
            Sort By
          </span>
        <Dropdown className='d-inline mx-2'>
          <Dropdown.Toggle variant="success" id="dropdown-basic">
            {sort}
          </Dropdown.Toggle>

          <Dropdown.Menu>
            <Dropdown.Item onClick={handleSort}>Views Ascending</Dropdown.Item>
            <Dropdown.Item onClick={handleSort}>Views Descending</Dropdown.Item>
            <Dropdown.Item onClick={handleSort}>Likes Ascending</Dropdown.Item>
            <Dropdown.Item onClick={handleSort}>Likes Descending</Dropdown.Item>
            <Dropdown.Item onClick={handleSort}>Dislikes Ascending</Dropdown.Item>
            <Dropdown.Item onClick={handleSort}>Dislikes Descending</Dropdown.Item>
            <Dropdown.Item onClick={handleSort}>Comments Ascending</Dropdown.Item>
            <Dropdown.Item onClick={handleSort}>Comments Descending</Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
        </div>
        <button type="submit">submit</button>
      </form>
    </div>
  )
}
export default SearchForm