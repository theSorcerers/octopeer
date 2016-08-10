class Api::MouseClickEventsController < ApplicationController
  include Epochable
  include Showable
  include Indexable
  include Createable

  private

  def mouse_click_event_params
    params.require(:mouse_click_event).permit(:session_id, :created_at)
  end
end
