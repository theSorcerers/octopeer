class Api::WindowResolutionEventsController < ApplicationController
  include Epochable
  include Showable
  include Indexable
  include Createable

  private

  def window_resolution_event_params
    params.require(:window_resolution_event).permit(:width, :height, :session_id, :created_at)
  end
end
