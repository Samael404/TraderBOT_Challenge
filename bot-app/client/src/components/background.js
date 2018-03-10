import React, { Component } from 'react';
import BackgroundSlideshow from 'react-background-slideshow';

import image1 from '../images/001.jpg';
import image2 from '../images/002.jpg';

class Show extends Component {
    render () {
        return (
            <div>
                <BackgroundSlideshow images= {[ image1, image2 ]} />
            </div>
        )
    }
}

export default Show;