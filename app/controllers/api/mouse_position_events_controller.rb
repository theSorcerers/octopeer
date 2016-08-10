class Api::MousePositionEventsController < ApplicationController
  include Epochable
  include Showable
  include Indexable
  include Createable

  private

  def mouse_position_event_params
    params.require(:mouse_position_event).permit(:position_x, :position_y, :viewport_x, :viewport_y, :session_id, :created_at)
  end
end
